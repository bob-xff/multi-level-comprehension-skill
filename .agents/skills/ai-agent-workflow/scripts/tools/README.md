# AI智能体5级用法工作流 - 辅助工具

本目录包含AI智能体5级用法工作流的辅助工具和脚本。

## 目录结构

```
tools/
├── context_builder.py          # ★ 项目上下文构建器（企业级核心）
├── code_quality_checker.py     # 代码质量检查工具
├── automated_tester.py         # 自动化测试工具
├── project_initializer.py      # 项目初始化工具
└── README.md                   # 本文件
```

## 工具说明

### 0. 项目上下文构建器（★ 企业级核心工具）

**文件:** `context_builder.py`

**功能:**
- 扫描项目结构，生成带职责推测的目录树
- 检测技术栈、框架、工程化配置（CI/格式化/测试框架）
- 读取README摘要和最近Git提交，还原项目演变脉络
- 自动生成"上下文注入块"——复制给AI即可开始工作
- 引导生成四个认知文件（PROJECT_BRIEF/ARCHITECTURE/CONVENTIONS/GLOSSARY）

**使用方法:**
```bash
# 扫描当前项目并输出到终端
python tools/context_builder.py

# 扫描指定项目并保存
python tools/context_builder.py /path/to/project --output CONTEXT.md

# 限制展示的文件数量（默认60）
python tools/context_builder.py . --max-files 100
```

**适用场景:** 新接手项目、AI首次接触代码库、大项目开始一个新模块之前。生成结果建议人工修订关键信息后，固化到项目的认知文件体系中。

### 1. 代码质量检查工具

**文件:** `code_quality_checker.py`

**功能:**
- 自动检查Python/JavaScript代码格式
- 扫描安全漏洞
- 评估代码质量
- 生成质量报告

**使用方法:**
```bash
# 检查单个文件
python tools/code_quality_checker.py src/main.py

# 检查整个目录
python tools/code_quality_checker.py src/
```

**检查项目:**
- **格式检查:** 使用black(Python)或prettier(JavaScript)
- **安全检查:** 使用bandit(Python)或npm audit(JavaScript)
- **质量检查:** 使用pylint(Python)或eslint(JavaScript)

**输出示例:**
```
============================================================
AI智能体5级用法工作流 - 代码质量报告
============================================================
生成时间: 2026-09-01 15:30:00
检查文件数: 5

------------------------------------------------------------
总体评分
------------------------------------------------------------
格式评分: 85.0%
安全评分: 92.0%
质量评分: 78.0%
总体评分: 85.0%
```

### 2. 自动化测试工具

**文件:** `automated_tester.py`

**功能:**
- 自动运行单元测试
- 自动运行集成测试
- 自动运行性能测试
- 生成测试报告

**使用方法:**
```bash
# 运行单元测试
python tools/automated_tester.py unit tests/

# 运行集成测试
python tools/automated_tester.py integration tests/integration/

# 运行性能测试
python tools/automated_tester.py performance tests/performance/
```

**测试类型:**
- **unit:** 单元测试
- **integration:** 集成测试
- **performance:** 性能测试

**输出示例:**
```
============================================================
AI智能体5级用法工作流 - 自动化测试报告
============================================================
生成时间: 2026-09-01 15:30:00

------------------------------------------------------------
总体统计
------------------------------------------------------------
总测试数: 50
通过测试: 48
失败测试: 2
跳过测试: 0
平均覆盖率: 85.0%
总测试时长: 12.50秒
总体成功率: 96.0%
```

### 3. 项目初始化工具

**文件:** `project_initializer.py`

**功能:**
- 自动创建项目结构
- 生成配置文件
- 创建文档模板
- 配置CI/CD

**使用方法:**
```bash
# 创建Python API项目
python tools/project_initializer.py my-project --type api --lang python --framework flask

# 创建JavaScript Web项目
python tools/project_initializer.py my-app --type web --lang javascript --framework react

# 创建Python库项目
python tools/project_initializer.py my-lib --type library --lang python
```

**项目类型:**
- **web:** Web前端项目
- **api:** API后端项目
- **library:** 库项目
- **cli:** 命令行工具项目

**编程语言:**
- **python:** Python项目
- **javascript:** JavaScript项目
- **typescript:** TypeScript项目

**框架:**
- **flask:** Flask (Python)
- **django:** Django (Python)
- **fastapi:** FastAPI (Python)
- **express:** Express (JavaScript)
- **react:** React (JavaScript)
- **vue:** Vue.js (JavaScript)

**功能特性:**
- **auth:** 认证功能
- **cache:** 缓存功能
- **queue:** 消息队列功能
- **monitoring:** 监控功能

**输出示例:**
```
✅ 项目 'my-project' 创建成功!
📁 项目目录: ./my-project

✅ 项目初始化完成!
📁 进入项目目录: cd my-project
🚀 开始开发吧!
```

## 环境要求

### Python工具

```bash
# 安装Python依赖
pip install black bandit pylint pytest

# 或者使用requirements.txt
pip install -r requirements-tools.txt
```

### JavaScript工具

```bash
# 安装JavaScript工具
npm install -g prettier eslint jest

# 或者使用package.json
npm install
```

## 集成到工作流

### 1. 代码提交前检查

在提交代码前运行质量检查：

```bash
# 检查代码质量
python tools/code_quality_checker.py src/

# 如果有问题，修复后重新检查
python tools/code_quality_checker.py src/
```

### 2. 持续集成

在CI/CD流程中集成测试：

```yaml
# .github/workflows/ci.yml
- name: Run tests
  run: python tools/automated_tester.py unit tests/

- name: Check code quality
  run: python tools/code_quality_checker.py src/
```

### 3. 项目初始化

使用工具快速创建新项目：

```bash
# 创建新项目
python tools/project_initializer.py new-project --type api --lang python --framework fastapi

# 进入项目
cd new-project

# 开始开发
python src/main.py
```

## 自定义配置

### 配置文件

工具支持自定义配置文件：

```yaml
# config.yml
quality:
  format:
    tool: black
    line_length: 88
  security:
    tool: bandit
    severity: medium
  quality:
    tool: pylint
    min_score: 8.0

testing:
  framework: pytest
  coverage_threshold: 80
  timeout: 300

project:
  template_dir: ./templates
  output_dir: ./output
```

### 使用配置文件

```bash
# 使用配置文件
python tools/code_quality_checker.py src/ --config config.yml
python tools/automated_tester.py unit tests/ --config config.yml
python tools/project_initializer.py my-project --config config.yml
```

## 常见问题

### Q1: 工具安装失败

**A:** 确保已安装Python 3.8+和pip。如果安装失败，尝试：

```bash
# 升级pip
pip install --upgrade pip

# 使用国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple black
```

### Q2: 工具运行报错

**A:** 检查文件路径是否正确，确保文件存在且有读取权限。

### Q3: 如何添加自定义检查规则

**A:** 修改工具源代码或使用配置文件添加自定义规则。

## 更新日志

### v1.0.0 (2026-09-01)

- ✨ 初始版本
- ✨ 代码质量检查工具
- ✨ 自动化测试工具
- ✨ 项目初始化工具

---

*最后更新：2026年9月1日*
