# Multi-level Comprehension Skill

> AI智能体5级使用方法工作流 - 适用于所有AI编程助手和智能体工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-3.0.0-blue.svg)](https://github.com/bob-xff/multi-level-comprehension-skill)

## 📋 项目简介

这是一个完整的AI智能体使用方法论框架，基于"南吴NANWU"在抖音视频中分享的"18天跑400个任务"的实践总结，将其封装为可多次引用的ZCode技能（Skill）。

**核心特点：**
- 🎯 **5级使用框架** - 从基础代码生成到自主项目管理
- 🔧 **通用设计** - 适用于所有AI编程工具
- 🧠 **企业级认知注入（v3.0）** - 项目认知文件体系 + 上下文构建器，让AI真正理解项目目的
- 📋 **需求澄清协议（v3.0）** - 先理解再行动：复述 → 假设 → 澄清 → 方案先行
- 🔍 **自我审查机制（v3.0）** - 交付前AI自审 + 质量门禁
- 📚 **完整文档** - 详细的指南、模板与ADR
- 🛠️ **自动化工具** - 上下文构建、代码质量检查、自动化测试、项目初始化

## 🚀 快速开始

### 1. 安装/使用

#### 方式一：直接使用（推荐）

```bash
# 克隆仓库
git clone https://github.com/your-username/multi-level-comprehension-skill.git

# 进入目录
cd multi-level-comprehension-skill
```

#### 方式二：作为ZCode Skill使用

将 `.agents/skills/ai-agent-workflow` 目录复制到你的项目中：

```bash
# 复制skill到你的项目
cp -r .agents/skills/ai-agent-workflow /path/to/your/project/.agents/skills/
```

### 2. 选择合适的级别

根据任务复杂度选择使用级别：

| 级别 | 适用场景 | 复杂度 | 示例 |
|------|----------|--------|------|
| **第1级** | 快速原型、小功能 | 低 | 编写函数、代码片段 |
| **第2级** | 项目维护、Bug修复 | 中 | 重构代码、修复问题 |
| **第3级** | 功能模块开发 | 中高 | API接口、数据库操作 |
| **第4级** | 架构设计、系统优化 | 高 | 系统重构、性能优化 |
| **第5级** | 端到端功能交付 | 极高 | 完整项目开发 |

### 3. 使用工具

#### 代码质量检查

```bash
# 检查Python代码
python .agents/skills/ai-agent-workflow/scripts/tools/code_quality_checker.py src/

# 检查JavaScript代码
python .agents/skills/ai-agent-workflow/scripts/tools/code_quality_checker.py src/
```

#### 自动化测试

```bash
# 运行单元测试
python .agents/skills/ai-agent-workflow/scripts/tools/automated_tester.py unit tests/

# 运行集成测试
python .agents/skills/ai-agent-workflow/scripts/tools/automated_tester.py integration tests/
```

#### 项目初始化

```bash
# 创建Python API项目
python .agents/skills/ai-agent-workflow/scripts/tools/project_initializer.py my-project --type api --lang python --framework flask

# 创建JavaScript Web项目
python .agents/skills/ai-agent-workflow/scripts/tools/project_initializer.py my-app --type web --lang javascript --framework react
```

## 📚 使用示例

### 示例1：使用Codex实现功能

```markdown
#file: src/services/user_service.py
#file: src/models/user.py

请在 user_service.py 中实现用户注册功能，
参考 user.py 中的数据模型。

要求：
- 参数验证
- 密码加密
- 返回用户对象
- 添加错误处理
```

### 示例2：使用Copilot编写代码

```python
# 实现用户注册功能
# 接收用户名、邮箱、密码参数
# 验证参数格式
# 检查用户名和邮箱是否已存在
# 加密密码
# 保存到数据库
# 返回用户对象
def register_user(username: str, email: str, password: str) -> User:
```

### 示例3：使用Claude分析代码

```
我有一个用户管理系统，需要实现注册功能。

项目结构：
- models/user.py：用户模型
- services/auth.py：认证服务
- controllers/user_controller.py：用户控制器

请帮我：
1. 在 auth.py 中实现 register 方法
2. 在 user_controller.py 中添加注册接口
3. 编写单元测试

[上传相关文件]
```

### 示例4：使用GPT-4设计架构

```
你是一个资深的Python开发工程师。

请帮我设计一个用户权限管理系统，要求：

1. 功能需求：
   - 用户角色管理（RBAC）
   - 资源权限控制
   - 权限分配和回收
   - 操作日志记录

2. 技术约束：
   - 使用Spring Boot框架
   - MySQL数据库
   - Redis缓存
   - JWT认证

请提供：
1. 数据库设计
2. 系统架构
3. 核心接口设计
4. 实施计划
```

### 示例5：使用Cursor重构代码

```
@src/services/auth.py
@src/models/user.py

请重构 auth.py 中的 login 方法：
1. 添加参数验证
2. 改进错误处理
3. 添加日志记录
4. 优化数据库查询
```

## 🛠️ 工具说明

### 1. 代码质量检查工具

**文件：** `scripts/tools/code_quality_checker.py`

**功能：**
- 自动检查Python/JavaScript代码格式
- 扫描安全漏洞
- 评估代码质量
- 生成质量报告

**使用方法：**
```bash
# 检查单个文件
python scripts/tools/code_quality_checker.py src/main.py

# 检查整个目录
python scripts/tools/code_quality_checker.py src/
```

**检查项目：**
- **格式检查：** 使用black(Python)或prettier(JavaScript)
- **安全检查：** 使用bandit(Python)或npm audit(JavaScript)
- **质量检查：** 使用pylint(Python)或eslint(JavaScript)

### 2. 自动化测试工具

**文件：** `scripts/tools/automated_tester.py`

**功能：**
- 自动运行单元测试
- 自动运行集成测试
- 自动运行性能测试
- 生成测试报告

**使用方法：**
```bash
# 运行单元测试
python scripts/tools/automated_tester.py unit tests/

# 运行集成测试
python scripts/tools/automated_tester.py integration tests/integration/

# 运行性能测试
python scripts/tools/automated_tester.py performance tests/performance/
```

### 3. 项目初始化工具

**文件：** `scripts/tools/project_initializer.py`

**功能：**
- 自动创建项目结构
- 生成配置文件
- 创建文档模板
- 配置CI/CD

**使用方法：**
```bash
# 创建Python API项目
python scripts/tools/project_initializer.py my-project --type api --lang python --framework flask

# 创建JavaScript Web项目
python scripts/tools/project_initializer.py my-app --type web --lang javascript --framework react

# 创建Python库项目
python scripts/tools/project_initializer.py my-lib --type library --lang python
```

**项目类型：**
- `web` - Web前端项目
- `api` - API后端项目
- `library` - 库项目
- `cli` - 命令行工具项目

**编程语言：**
- `python` - Python项目
- `javascript` - JavaScript项目
- `typescript` - TypeScript项目

**框架：**
- `flask` - Flask (Python)
- `django` - Django (Python)
- `fastapi` - FastAPI (Python)
- `express` - Express (JavaScript)
- `react` - React (JavaScript)
- `vue` - Vue.js (JavaScript)

## 📁 项目结构

```
multi-level-comprehension-skill/
├── .agents/
│   └── skills/
│       └── ai-agent-workflow/
│           ├── SKILL.md                          # 主技能文件
│           ├── README.md                         # 使用说明
│           ├── CHANGELOG.md                      # 版本变更日志
│           ├── assets/
│           │   └── quick-reference.md           # 快速参考卡
│           ├── references/
│           │   ├── detailed-guide.md            # 详细指南
│           │   ├── quality-metrics.md           # 质量指标体系
│           │   └── team-collaboration.md        # 团队协作指南
│           └── scripts/
│               ├── README.md                    # 脚本说明
│               ├── templates/                   # 提示词模板
│               │   ├── new-feature.md          # 新功能开发模板
│               │   ├── bug-fix.md             # Bug修复模板
│               │   ├── refactor.md            # 代码重构模板
│               │   └── architecture.md        # 架构设计模板
│               ├── checklists/                  # 检查清单
│               │   ├── code-review.md          # 代码审查清单
│               │   ├── testing.md             # 测试验证清单
│               │   └── security.md            # 安全检查清单
│               └── tools/                       # 辅助工具
│                   ├── README.md              # 工具说明文档
│                   ├── code_quality_checker.py # 代码质量检查工具
│                   ├── automated_tester.py    # 自动化测试工具
│                   └── project_initializer.py # 项目初始化工具
├── docs/                                        # 项目文档
│   ├── api.md                                  # API文档
│   └── deploy.md                               # 部署文档
├── README.md                                    # 本文件
├── LICENSE                                      # MIT许可证
└── .gitignore                                   # Git忽略文件
```

## 🎯 适用工具

本框架适用于所有AI编程工具，包括但不限于：

### 📌 云端AI智能体
- OpenAI Codex
- Devin AI
- OpenHands (原OpenDevin)
- SWE-agent
- AutoCodeRover

### 📌 IDE集成AI助手
- GitHub Copilot
- Cursor
- Windsurf
- JetBrains AI Assistant
- Amazon Q Developer
- Sourcegraph Cody

### 📌 代码补全工具
- Tabnine
- Codeium
- Supermaven
- Tabby
- Continue.dev

### 📌 通用AI助手
- GPT-4/ChatGPT
- Claude
- Google Gemini
- Microsoft Copilot

### 📌 开源AI工具
- Aider
- LLaMA Code
- StarCoder
- CodeLlama
- DeepSeek Coder

## 📖 文档

- [详细指南](.agents/skills/ai-agent-workflow/references/detailed-guide.md)
- [快速参考卡](.agents/skills/ai-agent-workflow/assets/quick-reference.md)
- [质量指标体系](.agents/skills/ai-agent-workflow/references/quality-metrics.md)
- [团队协作指南](.agents/skills/ai-agent-workflow/references/team-collaboration.md)
- [工具使用说明](.agents/skills/ai-agent-workflow/scripts/tools/README.md)

## 🤝 贡献

欢迎贡献代码、提出问题或建议！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证

本项目基于MIT许可证开源 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢"南吴NANWU"提供的实践总结
- 感谢社区贡献的模板和工具
- 感谢所有使用者的反馈和建议

---

**最后更新：** 2026年9月
**版本：** v3.0.0（企业级增强版）
