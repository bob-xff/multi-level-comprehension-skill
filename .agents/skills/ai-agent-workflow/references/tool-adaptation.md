# 工具适配详细指南（Tool Adaptation Guide）

> 本文件是SKILL.md"五、工具适配速查"的详细版，包含各工具的最佳实践与完整示例。
> 所有示例均遵循SKILL.md的核心理念：先理解再行动、精确约束、自我审查。

## 通用原则（无论用什么工具都适用）

1. **清晰的任务描述** —— 具体、有约束、有验收标准
2. **完整的上下文** —— 认知文件 + 相关代码 + 风格样例
3. **分阶段执行** —— 复杂任务先方案后执行
4. **交付前自审** —— 对照SKILL.md步骤6的审查清单

---

## 1. OpenAI Codex

**特点：** 云端执行，自主性强
**最佳实践：**
- 使用 `#file` 引用项目文件
- 明确任务分解和验收标准
- 第4-5级任务先让它输出执行计划

**示例：**
```
#file: src/services/user_service.py
#file: src/models/user.py
#file: PROJECT_BRIEF.md

请在 user_service.py 中实现用户注册功能，参考 user.py 数据模型。
执行前先输出修改方案，确认后执行。

要求：
- 参数验证（用户名3-20字符、密码8位以上含大小写数字）
- 密码bcrypt加密
- 用户名/邮箱重复返回明确错误码
- 返回用户对象
```

## 2. GitHub Copilot

**特点：** 实时补全，上下文感知
**最佳实践：**
- 编写清晰的注释作为"提示词"
- 提供函数签名和类型
- 用描述性命名引导补全

**示例：**
```python
# 实现用户注册功能
# 约束：接收用户名、邮箱、密码；验证格式；检查重复；bcrypt加密；返回User对象
def register_user(username: str, email: str, password: str) -> User:
```

## 3. Claude

**特点：** 长上下文，深度分析
**最佳实践：**
- 上传相关文件或粘贴完整上下文
- 复杂任务先要求输出方案再执行
- 明确"信息不足请直接说，不要编造"

**示例：**
```
我有一个用户管理系统，需要实现注册功能。

项目背景：[PROJECT_BRIEF 一段]
项目结构：
- models/user.py：用户模型
- services/auth.py：认证服务
- controllers/user_controller.py：用户控制器

请按 Clarify Protocol 执行：先复述需求、列出假设、提出澄清问题；
然后给出实施方案；我确认后你再写代码。最后交付前按自审清单检查。

如果以上信息不足，直接告诉我缺什么，不要基于假设编写。
```

## 4. GPT-4/ChatGPT

**特点：** 通用能力强，交互灵活
**最佳实践：**
- 明确角色设定
- 分步骤提问
- 要求解释思路

**示例：**
```
你是一名拥有15年经验的Python后端专家，特别擅长FastAPI和数据库设计。

请帮我实现用户注册功能：

1. 技术栈：Python 3.11 / FastAPI / SQLAlchemy / PostgreSQL
2. 功能要求：
   - 用户名、邮箱、密码注册
   - 参数验证（Pydantic）
   - bcrypt密码加密
   - 返回JWT token
3. 代码规范：PEP 8、完整类型注解、docstring

执行方式：先输出设计方案（表结构+接口定义+文件划分），
我确认后给出完整实现，交付前附自审结果。
```

## 5. Cursor

**特点：** IDE集成，代码感知
**最佳实践：**
- 用 `@` 精确引用文件，避免让AI自己猜
- 选中代码后修改，缩小范围
- 利用 .cursorrules 固化项目约定（把CONVENTIONS.md内容放进去）

**示例：**
```
@src/services/auth.py
@src/models/user.py
@CONVENTIONS.md

请重构 auth.py 中的 login 方法，遵守 CONVENTIONS.md 约定：
1. 添加参数验证
2. 改进错误处理（统一抛 BizException）
3. 添加日志记录
4. 优化数据库查询（避免N+1）
```

## 6. Windsurf

**特点：** 全栈开发，智能补全
**最佳实践：**
- 利用项目级上下文
- 自然语言描述 + 明确验收标准

**示例：**
```
创建用户管理API模块：

1. 文件结构：
   - src/api/users.py
   - src/services/user_service.py
   - src/models/user.py

2. 接口：
   - POST /api/users/register
   - POST /api/users/login
   - GET /api/users/me

3. 验收标准：RESTful设计、JWT认证、输入验证、统一错误处理、单元测试全通过
```

## 7. Devin AI

**特点：** 自主AI软件工程师，可独立完成复杂任务
**最佳实践：**
- 提供完整项目认知（第0步认知注入对Devin尤其重要）
- 设置明确验收标准和边界
- 要求分阶段汇报

**示例：**
```
任务：实现用户认证系统

项目信息：
- 项目认知：[PROJECT_BRIEF.md 全文]
- 技术栈：Python + FastAPI + PostgreSQL
- 仓库：[仓库链接]

需求：
1. 用户注册（邮箱+密码）
2. 登录（JWT）
3. 密码重置
4. 权限管理

工作方式：
1. 先输出任务分解，等我确认
2. 每完成一个任务提交一次，附说明
3. 遇到不确定的决策，停下来问我，不要自作主张

验收标准：
- 所有测试通过
- 符合 CONVENTIONS.md 约定
- 附使用文档
```

## 8. Replit AI

**特点：** 在线IDE集成AI，支持多人协作
**最佳实践：**
- 利用内置包管理和部署
- 小项目直接全流程交付

**示例：**
```
创建一个Flask Web应用：
1. 结构：main.py / requirements.txt / templates/
2. 功能：用户注册登录、文章发布、REST API
3. 部署：使用Replit部署，环境变量配置数据库连接
```

## 9. Tabnine

**特点：** 本地AI代码补全，保护隐私
**最佳实践：**
- 编写清晰的docstring和类型注解引导补全
- 团队统一代码风格提升补全质量

**示例：**
```python
def process_order(order_id: int) -> Order:
    """处理订单：校验存在性→检查库存→扣减→返回订单对象
    Args:
        order_id: 订单ID
    Returns:
        处理后的订单对象
    Raises:
        OrderNotFoundError: 订单不存在时
    """
```

## 10. Amazon Q Developer

**特点：** AWS生态集成，安全扫描
**最佳实践：**
- 利用AWS服务集成和安全扫描
- 遵循最小权限

**示例：**
```
创建一个AWS Lambda函数：
1. 触发器：S3 ObjectCreated
2. 逻辑：读取文件→解析JSON→存DynamoDB
3. 安全：IAM最小权限、环境变量加密、完整错误处理
```

## 11. JetBrains AI Assistant

**特点：** JetBrains IDE深度集成
**最佳实践：**
- 结合IDE的代码分析能力
- 重构类任务优先用它（对IDE重构动作感知最好）

**示例：**
```
重构用户服务模块：
当前问题：1. 函数过长 2. 重复代码 3. 缺少错误处理
目标：拆分小函数、提取公共方法、添加异常处理、保持向后兼容
```

## 12. Sourcegraph Cody

**特点：** 代码搜索和AI理解
**最佳实践：**
- 跨库理解类任务优先
- 让它先"讲清楚现有实现"，再讨论改动

**示例：**
```
分析用户认证的完整调用链：从请求进入到token生成。
先输出调用链和数据流图，确认理解无误后，再指出可优化的3个点。
```

## 13. Aider

**特点：** 开源AI配对编程，Git集成
**最佳实践：**
- 用 /add 精确控制文件范围
- 一次一个逻辑改动，勤提交
- 用CONVENTIONS内容定制CONVENTIONS.md（Aider原生支持）

**示例：**
```bash
aider --model gpt-4
> /add src/services/auth.py src/models/user.py
> 请实现用户注册功能。先说明修改方案再动手，
> 修改后运行 pytest tests/test_auth.py 验证。
```

## 14. 开源/本地模型（DeepSeek Coder, StarCoder, Tabby等）

**最佳实践：**
- 本地部署保护代码隐私
- 提示词格式标准化（它们对结构化提示词更敏感）
- 复杂任务拆小（上下文窗口相对有限）

**示例：**
```
任务：[一句话]
上下文：[文件路径 + 粘贴相关代码]
要求：1. [...] 2. [...]
约束：[...]
输出：只输出代码，不要解释。
```

## 15. 通用AI助手（Gemini, Microsoft Copilot, Perplexity, Phind等）

**最佳实践：**
- 角色设定 + 完整上下文 + 分步提问
- 适合第1-2级任务和方案讨论

**示例：**
```
你是资深[技术栈]工程师。任务：[描述]。
背景：[项目背景]
约束：[技术约束]
请提供：1. 设计方案 2. 实现代码 3. 测试要点
```

---

## 工具特性对比表

| 特性 | Codex | Copilot | Claude | GPT-4 | Cursor | Devin | Aider |
|---|---|---|---|---|---|---|---|
| 执行方式 | 云端 | 本地 | 云端 | 云端 | 本地 | 云端 | 本地 |
| 上下文方式 | `#file` | 自动 | 上传/粘贴 | 粘贴 | `@` | 仓库 | /add |
| 自主性 | 高 | 低 | 中 | 中 | 中 | 极高 | 中 |
| 响应速度 | 中 | 快 | 中 | 中 | 快 | 慢 | 中 |
| 最佳级别 | 3-5级 | 1-2级 | 2-5级 | 1-4级 | 1-3级 | 4-5级 | 2-4级 |

**选择决策树：**
```
任务复杂吗？
├─ 简单（1-2级）→ IDE集成类（Cursor/Copilot）实时补全
├─ 中等（3级）→ 对话式（Claude/GPT-4）或 Cursor
└─ 复杂（4-5级）
   ├─ 有成熟CI/CD和代码审查流程 → 云端智能体（Codex/Devin）
   └─ 需要强控制、分步确认 → 对话式（Claude）+ 七步工作流
```
