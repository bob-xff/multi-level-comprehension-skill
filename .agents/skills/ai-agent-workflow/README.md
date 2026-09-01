# AI智能体5级用法工作流 Skill

## 📁 目录结构

```
ai-agent-workflow/
├── SKILL.md                          # 主技能文件
├── README.md                        # 使用说明
├── CHANGELOG.md                     # 版本变更日志
├── assets/
│   └── quick-reference.md           # 快速参考卡
├── references/
│   ├── detailed-guide.md            # 详细指南
│   ├── quality-metrics.md           # 质量指标体系
│   └── team-collaboration.md        # 团队协作指南
└── scripts/
    ├── README.md                    # 脚本说明
    ├── templates/                   # 提示词模板
    │   ├── new-feature.md          # 新功能开发模板
    │   ├── bug-fix.md             # Bug修复模板
    │   ├── refactor.md            # 代码重构模板
    │   └── architecture.md        # 架构设计模板
    └── checklists/                  # 检查清单
        ├── code-review.md          # 代码审查清单
        ├── testing.md             # 测试验证清单
        └── security.md            # 安全检查清单
```

---

## 🚀 快速开始

### 1. 选择合适的工具

**本框架适用于所有AI智能体工具**，包括但不限于：

#### 📌 云端AI智能体
- OpenAI Codex - 云端软件工程智能体
- Devin AI - AI软件工程师
- OpenHands (原OpenDevin) - 开源AI开发智能体
- SWE-agent - 软件工程智能体
- AutoCodeRover - 自动代码修复智能体

#### 📌 IDE集成AI助手
- GitHub Copilot - 代码补全助手
- Cursor - AI代码编辑器
- Windsurf - AI开发环境
- JetBrains AI Assistant - JetBrains IDE集成AI
- Amazon Q Developer (原CodeWhisperer) - AWS代码助手
- Sourcegraph Cody - 代码搜索和AI助手

#### 📌 代码补全工具
- Tabnine - AI代码补全
- Codeium - 免费AI代码补全
- Supermaven - 快速AI代码补全
- Tabby - 开源AI代码助手
- Continue.dev - 开源AI代码助手

#### 📌 通用AI助手
- GPT-4/ChatGPT - OpenAI通用AI助手
- Claude - Anthropic的AI助手
- Google Gemini - Google AI助手
- Microsoft Copilot - Microsoft AI助手

#### 📌 开源AI工具
- Aider - AI配对编程工具
- LLaMA Code - Meta开源代码模型
- StarCoder - BigCode开源代码模型
- CodeLlama - Meta代码生成模型
- DeepSeek Coder - 深度求索代码模型

#### 📌 其他AI编程工具
- Replit AI - Replit集成AI助手
- Phind - AI编程搜索引擎
- **任何未来出现的新AI工具**

根据任务类型选择最合适的AI工具：

| 任务类型 | 推荐工具 | 原因 |
|----------|----------|------|
| 快速原型 | Copilot, Cursor, Codeium | 快速补全，IDE集成 |
| 代码审查 | Claude, GPT-4, Cody | 深度分析，通用能力强 |
| 架构设计 | Claude, GPT-4, Gemini | 长上下文，深度思考 |
| 复杂实现 | Codex, Devin, OpenHands | 自主性强，云端执行 |
| 日常编码 | Copilot, Tabnine, Continue | 实时补全，高效 |
| AWS项目 | Amazon Q Developer | AWS生态集成 |
| JetBrains | AI Assistant | IDE深度集成 |
| 开源需求 | Aider, Tabby, LLaMA Code | 开源，可自定义 |

### 2. 选择合适的级别

根据任务复杂度选择使用级别：

| 级别 | 适用场景 | 复杂度 |
|------|----------|--------|
| 第1级 | 快速原型、小功能 | 低 |
| 第2级 | 项目维护、Bug修复 | 中 |
| 第3级 | 功能模块开发 | 中高 |
| 第4级 | 架构设计、系统优化 | 高 |
| 第5级 | 端到端功能交付 | 极高 |

### 3. 使用模板

根据任务类型选择对应的模板：

- `new-feature.md` - 新功能开发模板
- `bug-fix.md` - Bug修复模板
- `refactor.md` - 代码重构模板
- `architecture.md` - 架构设计模板

### 4. 验证结果

使用检查清单验证生成的代码：

- `code-review.md` - 代码审查清单
- `testing.md` - 测试验证清单
- `security.md` - 安全检查清单

### 5. 企业级功能

对于团队使用，可参考以下文档：

- `CHANGELOG.md` - 版本变更日志
- `references/quality-metrics.md` - 质量指标体系
- `references/team-collaboration.md` - 团队协作指南

---

## 📖 使用示例

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

---

## 🛠️ 工具配置

### 通用配置

#### 代码风格
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

#### 测试配置
```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": ["tests"]
}
```

### 特定工具配置

#### Codex
```yaml
# codex.yaml
model: codex-1
temperature: 0.2
max_tokens: 4096
```

#### Copilot
```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true
  }
}
```

#### Cursor
```json
{
  "cursor.ai.enabled": true,
  "cursor.ai.model": "gpt-4"
}
```

---

## 📊 使用统计

### 工具使用频率

| 工具 | 适用场景 | 使用频率 |
|------|----------|----------|
| Copilot | 日常编码 | 高 |
| Cursor | IDE集成 | 高 |
| GPT-4 | 通用任务 | 中 |
| Claude | 深度分析 | 中 |
| Codex | 复杂任务 | 低 |

### 任务级别分布

| 级别 | 任务占比 | 平均耗时 |
|------|----------|----------|
| 第1级 | 40% | 10分钟 |
| 第2级 | 30% | 30分钟 |
| 第3级 | 20% | 2小时 |
| 第4级 | 8% | 1天 |
| 第5级 | 2% | 1周 |

---

## 🎯 最佳实践

### 1. 任务分解
- 将大任务拆分为小任务
- 每个任务有明确的目标
- 按依赖关系排序执行

### 2. 上下文管理
- 提供必要的代码上下文
- 说明技术约束和规范
- 分享业务需求和规则

### 3. 质量控制
- 使用检查清单验证
- 进行代码审查
- 执行测试验证

### 4. 迭代优化
- 根据反馈调整提示词
- 优化任务分解方式
- 持续改进工作流程

---

## 🔧 工具推荐

### 开发工具
- **IDE：** VS Code / PyCharm / IntelliJ IDEA
- **版本控制：** Git
- **包管理：** npm / pip / maven

### 测试工具
- **单元测试：** pytest / Jest / JUnit
- **集成测试：** Postman / RestAssured
- **性能测试：** JMeter / Locust

### 代码质量
- **静态分析：** ESLint / Pylint / SonarQube
- **格式化：** Prettier / Black / clang-format
- **类型检查：** TypeScript / MyPy

---

## 📚 学习路径

### 初学者路径
1. 阅读 `SKILL.md` 了解整体框架
2. 使用 `assets/quick-reference.md` 快速上手
3. 使用 `scripts/templates/new-feature.md` 实践
4. 使用 `scripts/checklists/code-review.md` 自查

### 进阶路径
1. 阅读 `references/detailed-guide.md` 深入理解
2. 使用所有模板处理不同场景
3. 使用所有检查清单保证质量
4. 根据项目需求定制模板

### 专家路径
1. 基于现有模板创建自定义模板
2. 优化检查清单适应项目需求
3. 建立团队最佳实践
4. 贡献新的模板和工具

### 企业级路径
1. 阅读 `CHANGELOG.md` 了解版本管理
2. 参考 `references/quality-metrics.md` 建立质量指标
3. 参考 `references/team-collaboration.md` 建立协作规范
4. 集成到CI/CD流程实现自动化

---

## 🤝 贡献指南

### 添加新模板
1. 在 `scripts/templates/` 创建新文件
2. 遵循现有模板格式
3. 包含完整的字段说明
4. 提供使用示例

### 改进检查清单
1. 根据实际使用情况调整
2. 添加新的检查项
3. 移除不必要的检查项
4. 更新使用说明

### 报告问题
1. 描述遇到的问题
2. 提供复现步骤
3. 提供改进建议
4. 联系维护者

---

## 📄 许可证

本技能基于 MIT 许可证开源。

---

## 🙏 致谢

- 感谢"南吴NANWU"提供的实践总结
- 感谢社区贡献的模板和工具
- 感谢所有使用者的反馈和建议

---

*最后更新：2026年9月1日*