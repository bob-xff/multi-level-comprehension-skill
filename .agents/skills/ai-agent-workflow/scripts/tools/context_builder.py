#!/usr/bin/env python3
"""
AI智能体5级用法工作流 - 项目上下文构建器

扫描项目结构，自动生成"项目上下文包"，用于注入给AI。
输出内容包括：
1. 项目结构树（含各目录职责推测）
2. 认知文件骨架（PROJECT_BRIEF/ARCHITECTURE/CONVENTIONS/GLOSSARY 的 AI 生成草稿）
3. 技术栈检测
4. 一份可直接复制给AI的【上下文注入块】

用法:
    python context_builder.py [项目路径] [--output 上下文包输出路径] [--max-files N]
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

# 需要忽略的目录
IGNORED_DIRS = {
    "node_modules", "__pycache__", ".git", ".svn", "venv", ".venv", "env",
    "dist", "build", "target", ".idea", ".vscode", ".pytest_cache",
    ".mypy_cache", "coverage", ".next", ".nuxt", "vendor", "bin", "obj",
    ".gradle", ".mvn", ".terraform", ".tox", ".nox", "htmlcov", "site-packages",
}

# 常见职责推测表（目录名 -> 职责描述）
DIR_MEANINGS = {
    "src": "源代码主目录",
    "app": "应用主目录",
    "api": "API接口层",
    "routes": "路由定义",
    "controllers": "控制器层（请求处理）",
    "views": "视图/表现层",
    "services": "业务逻辑层",
    "models": "数据模型层",
    "entities": "实体定义",
    "repositories": "数据访问层",
    "dao": "数据访问层",
    "migrations": "数据库迁移脚本",
    "utils": "工具函数",
    "helpers": "辅助函数",
    "common": "公共模块",
    "core": "核心逻辑",
    "config": "配置",
    "settings": "配置",
    "tests": "测试代码",
    "test": "测试代码",
    "docs": "文档",
    "scripts": "构建/运维脚本",
    "components": "UI组件",
    "pages": "页面组件",
    "hooks": "Hooks（前端）",
    "store": "状态管理",
    "static": "静态资源",
    "assets": "静态资源",
    "templates": "模板文件",
    "lib": "第三方封装/库代码",
    "plugins": "插件",
    "middleware": "中间件",
    "auth": "认证授权",
    "domain": "领域模型",
    "dto": "数据传输对象",
    "schemas": "数据校验/Schema",
    "workers": "后台任务",
    "tasks": "后台任务",
    "jobs": "后台任务",
}

# 技术栈检测特征文件
TECH_STACK_MARKERS = {
    "requirements.txt": "Python (pip)",
    "pyproject.toml": "Python (modern)",
    "setup.py": "Python (legacy packaging)",
    "Pipfile": "Python (pipenv)",
    "package.json": "JavaScript/Node.js",
    "pom.xml": "Java (Maven)",
    "build.gradle": "Java/Kotlin (Gradle)",
    "go.mod": "Go",
    "Cargo.toml": "Rust",
    "composer.json": "PHP (Composer)",
    "Gemfile": "Ruby (Bundler)",
    "*.csproj": "C#/.NET",
    "Dockerfile": "Docker",
    "docker-compose.yml": "Docker Compose",
    "Makefile": "Make",
}

# 框架检测特征（在依赖文件中搜索）
FRAMEWORK_MARKERS = {
    "python": {
        "flask": "Flask", "fastapi": "FastAPI", "django": "Django",
        "sqlalchemy": "SQLAlchemy", "celery": "Celery", "redis": "Redis",
        "pydantic": "Pydantic", "pytest": "pytest",
    },
    "javascript": {
        "react": "React", "vue": "Vue.js", "angular": "Angular",
        "express": "Express", "next": "Next.js", "nuxt": "Nuxt",
        "typescript": "TypeScript", "jest": "Jest", "vite": "Vite",
    },
}


def detect_tech_stack(root: Path) -> dict:
    """检测项目技术栈"""
    stack = {"languages": [], "frameworks": [], "build_tools": []}

    # 检测特征文件
    found_markers = []
    for marker, name in TECH_STACK_MARKERS.items():
        if "*" in marker:
            matches = list(root.glob(f"**/{marker}"))
            if matches:
                found_markers.append(name)
        elif (root / marker).exists():
            found_markers.append(name)

    # 检测框架
    for req_file in ("requirements.txt", "package.json", "pyproject.toml"):
        f = root / req_file
        if not f.exists():
            continue
        try:
            content = f.read_text(encoding="utf-8", errors="ignore").lower()
        except Exception:
            continue
        lang = "python" if "python" in req_file or "requirements" in req_file else "javascript"
        for key, name in FRAMEWORK_MARKERS.get(lang, {}).items():
            if key in content and name not in stack["frameworks"]:
                stack["frameworks"].append(name)

    # 语言目录特征
    py_files = list(root.glob("**/*.py"))
    js_files = [f for f in root.glob("**/*.js") if "node_modules" not in str(f)]
    ts_files = [f for f in root.glob("**/*.ts") if "node_modules" not in str(f)]
    java_files = list(root.glob("**/*.java"))
    go_files = list(root.glob("**/*.go"))

    if py_files:
        stack["languages"].append(f"Python ({len(py_files)} files)")
    if ts_files:
        stack["languages"].append(f"TypeScript ({len(ts_files)} files)")
    if js_files:
        stack["languages"].append(f"JavaScript ({len(js_files)} files)")
    if java_files:
        stack["languages"].append(f"Java ({len(java_files)} files)")
    if go_files:
        stack["languages"].append(f"Go ({len(go_files)} files)")

    for m in found_markers:
        if m in ("Dockerfile", "Docker Compose", "Make"):
            stack["build_tools"].append(m)

    return stack


def build_tree(root: Path, max_depth: int = 4, max_files: int = 60) -> tuple:
    """构建目录树，并推测目录职责"""
    lines = []
    dir_purposes = {}
    file_count = 0

    def walk(d: Path, depth: int, prefix: str):
        nonlocal file_count
        if depth > max_depth or file_count > max_files:
            return
        try:
            entries = sorted(
                [e for e in d.iterdir() if e.name not in IGNORED_DIRS and not e.name.startswith(".git")],
                key=lambda x: (x.is_file(), x.name.lower()),
            )
        except PermissionError:
            return

        subdirs = [e for e in entries if e.is_dir()]
        files = [e for e in entries if e.is_file()]
        total = len(subdirs) + len(files)

        for i, entry in enumerate(subdirs):
            connector = "└── " if i == len(subdirs) - 1 and not files else "├── "
            purpose = DIR_MEANINGS.get(entry.name.lower(), "")
            if purpose:
                dir_purposes[str(entry.relative_to(root))] = purpose
            lines.append(f"{prefix}{connector}{entry.name}/" + (f"  # {purpose}" if purpose else ""))
            walk(entry, depth + 1, prefix + ("    " if i == len(subdirs) - 1 and not files else "│   "))

        for j, entry in enumerate(files):
            if file_count >= max_files:
                lines.append(f"{prefix}└── ... (其余文件省略)")
                break
            connector = "└── " if j == len(files) - 1 else "├── "
            lines.append(f"{prefix}{connector}{entry.name}")
            file_count += 1

    lines.append(f"{root.name}/")
    walk(root, 0, "")
    return "\n".join(lines), dir_purposes


def detect_conventions(root: Path) -> dict:
    """检测团队约定信号"""
    signals = {
        "formatter": [], "linter": [], "ci": [], "test_framework": [], "license": None,
    }
    checks = [
        (".pre-commit-config.yaml", "linter", "pre-commit"),
        ("setup.cfg", "linter", "setup.cfg (可能含flake8配置)"),
        (".flake8", "linter", "flake8"),
        ("pylintrc", "linter", "pylint"),
        (".eslintrc", "linter", "ESLint"),
        ("eslint.config.js", "linter", "ESLint (flat config)"),
        (".prettierrc", "formatter", "Prettier"),
        ("jest.config.js", "test_framework", "Jest"),
        (".github/workflows", "ci", "GitHub Actions"),
        (".gitlab-ci.yml", "ci", "GitLab CI"),
        ("Jenkinsfile", "ci", "Jenkins"),
        (".circleci", "ci", "CircleCI"),
        ("LICENSE", "license", "LICENSE文件存在"),
    ]
    for path, category, name in checks:
        p = root / path
        if p.exists():
            signals[category].append(name)
    return signals


def find_readme_summary(root: Path, max_chars: int = 800) -> str:
    """读取README前N字符作为项目摘要线索"""
    for name in ("README.md", "readme.md", "README.rst", "README.txt", "README"):
        p = root / name
        if p.exists():
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
                # 去掉markdown标记，取前max_chars字符
                text = re.sub(r"[#*`\[\]()!]", "", text)
                text = re.sub(r"\n{3,}", "\n\n", text).strip()
                return text[:max_chars]
            except Exception:
                pass
    return ""


def analyze_git_history(root: Path, max_commits: int = 5) -> list:
    """读取最近的git提交记录"""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "log", "--oneline", f"-{max_commits}"],
            capture_output=True, text=True, cwd=str(root), timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return [line.strip() for line in result.stdout.strip().split("\n")]
    except Exception:
        pass
    return []


def generate_context_package(root: Path) -> str:
    """生成完整的项目上下文包"""
    root = root.resolve()
    tree, dir_purposes = build_tree(root)
    stack = detect_tech_stack(root)
    conventions = detect_conventions(root)
    readme = find_readme_summary(root)
    git_log = analyze_git_history(root)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    sections = []

    # 头部
    sections.append(f"""# 项目上下文包（Context Package）
> 由 context_builder.py 自动生成于 {now}
> 用法：将本文件内容直接注入给AI作为任务上下文（L0层）。
> 建议流程：AI生成草稿 → 人工修订关键信息 → 固化为项目的四个认知文件。""")

    # 1. 项目概要线索
    summary_block = readme if readme else "（未检测到README，请人工补充项目定位）"
    sections.append(f"""
## 1. 项目概要线索（来自README，请人工校验）

{summary_block}""")

    # 2. 技术栈
    stack_lines = []
    if stack["languages"]:
        stack_lines.append("**语言：** " + ", ".join(stack["languages"]))
    if stack["frameworks"]:
        stack_lines.append("**框架/依赖：** " + ", ".join(stack["frameworks"]))
    if stack["build_tools"]:
        stack_lines.append("**构建工具：** " + ", ".join(stack["build_tools"]))
    if not stack_lines:
        stack_lines.append("（未检测到明确技术栈）")
    sections.append("## 2. 检测到的技术栈\n\n" + "\n".join(stack_lines))

    # 3. 项目结构
    sections.append(f"""
## 3. 项目结构（含职责推测）

```
{tree}
```""")

    # 4. 模块职责推测
    if dir_purposes:
        purpose_lines = [f"- `{k}/` - {v}" for k, v in sorted(dir_purposes.items())]
        sections.append("## 4. 模块职责（按目录名推测，请校验）\n\n" + "\n".join(purpose_lines))

    # 5. 工程化信号
    conv_lines = []
    if conventions["ci"]:
        conv_lines.append(f"- CI: {', '.join(conventions['ci'])}")
    if conventions["linter"]:
        conv_lines.append(f"- 静态检查: {', '.join(conventions['linter'])}")
    if conventions["formatter"]:
        conv_lines.append(f"- 格式化: {', '.join(conventions['formatter'])}")
    if conventions["test_framework"]:
        conv_lines.append(f"- 测试框架: {', '.join(conventions['test_framework'])}")
    if not conv_lines:
        conv_lines.append("- （未检测到明确的工程化配置）")
    sections.append("## 5. 工程化信号\n\n" + "\n".join(conv_lines))

    # 6. Git历史
    if git_log:
        log_lines = [f"- {c}" for c in git_log]
        sections.append("## 6. 最近提交（演变脉络线索）\n\n" + "\n".join(log_lines))

    # 7. 认知文件骨架
    sections.append("""
## 7. 待完善的认知文件（AI可据此起草，人工修订）

请基于以上信息，帮AI负责人起草以下四个文件（模板见 references/project-brief-template.md）：
- [ ] PROJECT_BRIEF.md —— 项目定位、业务目标、目标用户、Non-goals
- [ ] ARCHITECTURE.md —— 技术栈、分层结构、模块清单、数据流、技术债务
- [ ] CONVENTIONS.md —— 编码规范、目录约定、禁止事项、Git/测试约定
- [ ] GLOSSARY.md —— 领域术语表（含易混淆点）
""")

    # 8. 可直接注入的上下文块
    stack_str = "; ".join(stack["frameworks"]) or "未检测"
    purposes_str = "\n".join(f"  - {k}/: {v}" for k, v in list(sorted(dir_purposes.items()))[:10])
    sections.append(f"""
## 8. 快速注入块（复制给AI即可开始工作）

```
【项目认知】
- 项目定位：[请从上方第1节提炼一句话]
- 技术栈：{stack_str}
- 主要模块：
{purposes_str}

【任务】
[在此填写本次任务]

【约束】
- 遵循项目现有的分层结构和命名风格
- 不引入新的依赖，除非明确说明理由
- 信息不足时直接说明缺什么，不要编造

【工作方式】
- 先复述对项目和任务的理解，列出假设和澄清问题
- 给出实施方案（文件清单+改动点），确认后执行
- 交付前按自审清单检查（需求覆盖/边界/约束/测试/影响面）
```
""")

    return "\n---\n".join(sections)


def main():
    args = sys.argv[1:]
    project_path = "."
    output_file = None
    max_files = 60

    i = 0
    while i < len(args):
        if args[i] == "--output" and i + 1 < len(args):
            output_file = args[i + 1]
            i += 2
        elif args[i] == "--max-files" and i + 1 < len(args):
            max_files = int(args[i + 1])
            i += 2
        else:
            project_path = args[i]
            i += 1

    root = Path(project_path)
    if not root.exists():
        print(f"错误：路径不存在: {project_path}")
        sys.exit(1)
    if not root.is_dir():
        print(f"错误：{project_path} 不是目录")
        sys.exit(1)

    print(f"🔍 正在扫描项目: {root.resolve()}")
    package = generate_context_package(root)

    if output_file:
        Path(output_file).write_text(package, encoding="utf-8")
        print(f"✅ 上下文包已生成: {output_file}")
        print(f"📄 文件大小: {len(package)} 字符")
    else:
        print(package)
        print("\n💡 提示: 使用 --output CONTEXT.md 保存到文件")


if __name__ == "__main__":
    main()
