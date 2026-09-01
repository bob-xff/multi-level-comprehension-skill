# 安全检查清单

## 使用说明

本清单用于安全检查，帮助发现和修复安全漏洞。请在开发和测试过程中逐项检查。

---

## 一、输入验证

### 1.1 SQL注入防护
- [ ] 使用参数化查询
- [ ] 使用ORM框架
- [ ] 输入验证和过滤
- [ ] 最小权限原则
- [ ] 错误信息不泄露

```python
# 安全示例
# 正确：使用参数化查询
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

# 错误：字符串拼接
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
```

### 1.2 XSS攻击防护
- [ ] 输入验证和过滤
- [ ] 输出编码
- [ ] Content-Security-Policy
- [ ] HttpOnly Cookie
- [ ] 输入长度限制

```python
# 安全示例
# 正确：输出编码
from markupsafe import escape
safe_output = escape(user_input)

# 错误：直接输出
unsafe_output = user_input
```

### 1.3 CSRF攻击防护
- [ ] CSRF Token验证
- [ ] SameSite Cookie
- [ ] Referer/Origin验证
- [ ] 关键操作二次确认
- [ ] 自定义请求头

### 1.4 命令注入防护
- [ ] 避免执行系统命令
- [ ] 使用安全的API
- [ ] 输入验证
- [ ] 最小权限原则
- [ ] 沙箱执行

### 1.5 路径遍历防护
- [ ] 路径验证
- [ ] 使用白名单
- [ ] 避免用户输入直接拼接路径
- [ ] 使用安全的文件操作API
- [ ] 权限控制

---

## 二、认证安全

### 2.1 密码安全
- [ ] 密码强度要求
- [ ] 密码加密存储（bcrypt/scrypt）
- [ ] 密码历史记录
- [ ] 密码过期策略
- [ ] 密码重置安全

```python
# 安全示例
import bcrypt

# 正确：使用bcrypt加密
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# 错误：使用MD5/SHA1
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()
```

### 2.2 会话管理
- [ ] 会话ID安全生成
- [ ] 会话超时设置
- [ ] 会话固定防护
- [ ] 并发会话控制
- [ ] 会话注销功能

### 2.3 Token安全
- [ ] JWT Token安全
- [ ] Token过期设置
- [ ] Token刷新机制
- [ ] Token撤销功能
- [ ] Token存储安全

```python
# 安全示例
import jwt
from datetime import datetime, timedelta

# 正确：使用安全的JWT配置
payload = {
    "user_id": user_id,
    "exp": datetime.utcnow() + timedelta(hours=1),
    "iat": datetime.utcnow()
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# 错误：不设置过期时间
payload = {"user_id": user_id}
token = jwt.encode(payload, SECRET_KEY)
```

### 2.4 多因素认证
- [ ] 支持MFA
- [ ] TOTP实现
- [ ] 备份代码
- [ ] 恢复流程
- [ ] 设备管理

---

## 三、授权安全

### 3.1 权限控制
- [ ] 最小权限原则
- [ ] RBAC/ABAC实现
- [ ] 权限验证
- [ ] 权限粒度控制
- [ ] 权限审计

```python
# 安全示例
# RBAC权限检查
def check_permission(user, resource, action):
    """检查用户权限"""
    user_roles = get_user_roles(user)
    for role in user_roles:
        if has_permission(role, resource, action):
            return True
    return False

# 装饰器实现
def require_permission(resource, action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not check_permission(current_user, resource, action):
                raise PermissionDenied()
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 3.2 越权防护
- [ ] 水平越权防护
- [ ] 垂直越权防护
- [ ] 对象级权限控制
- [ ] 数据级权限控制
- [ ] 操作审计

### 3.3 API安全
- [ ] API认证
- [ ] API授权
- [ ] 速率限制
- [ ] 输入验证
- [ ] 输出过滤

---

## 四、数据安全

### 4.1 数据加密
- [ ] 传输加密（TLS）
- [ ] 存储加密
- [ ] 密钥管理
- [ ] 加密算法选择
- [ ] 加密实现

```python
# 安全示例
from cryptography.fernet import Fernet

# 正确：使用AES加密
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(plain_text.encode())
plain_text = cipher_suite.decrypt(cipher_text).decode()
```

### 4.2 敏感数据处理
- [ ] 敏感数据识别
- [ ] 数据脱敏
- [ ] 数据分类分级
- [ ] 数据访问控制
- [ ] 数据审计

```python
# 安全示例
def mask_sensitive_data(data):
    """脱敏敏感数据"""
    if "phone" in data:
        data["phone"] = data["phone"][:3] + "****" + data["phone"][-4:]
    if "email" in data:
        data["email"] = data["email"][:2] + "***" + data["email"][data["email"].index("@"):]
    if "id_card" in data:
        data["id_card"] = data["id_card"][:4] + "**********" + data["id_card"][-4:]
    return data
```

### 4.3 数据备份
- [ ] 备份策略
- [ ] 备份加密
- [ ] 备份验证
- [ ] 恢复测试
- [ ] 备份安全

### 4.4 数据销毁
- [ ] 安全删除
- [ ] 磁盘擦除
- [ ] 销毁记录
- [ ] 销毁验证
- [ ] 合规要求

---

## 五、日志安全

### 5.1 日志记录
- [ ] 安全事件记录
- [ ] 访问日志记录
- [ ] 操作日志记录
- [ ] 错误日志记录
- [ ] 审计日志记录

### 5.2 日志安全
- [ ] 敏感信息不记录
- [ ] 日志访问控制
- [ ] 日志完整性
- [ ] 日志加密
- [ ] 日志保留策略

```python
# 安全示例
import logging

# 正确：不记录敏感信息
logger.info("User login successful", extra={
    "user_id": user_id,
    "ip_address": ip_address
})

# 错误：记录密码
logger.info(f"User login: {username}, password: {password}")
```

### 5.3 日志分析
- [ ] 异常检测
- [ ] 攻击识别
- [ ] 入侵检测
- [ ] 安全告警
- [ ] 日志聚合

---

## 六、网络安全

### 6.1 传输安全
- [ ] TLS配置
- [ ] 证书管理
- [ ] HSTS配置
- [ ] 安全头配置
- [ ] 混合内容防护

```nginx
# 安全配置示例
# Nginx安全头配置
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Content-Security-Policy "default-src 'self'" always;
```

### 6.2 防火墙配置
- [ ] 入站规则
- [ ] 出站规则
- [ ] 端口管理
- [ ] IP白名单
- [ ] DDoS防护

### 6.3 网络隔离
- [ ] 网络分段
- [ ] 子网划分
- [ ] 访问控制
- [ ] 流量监控
- [ ] 入侵检测

---

## 七、应用安全

### 7.1 安全配置
- [ ] 默认账号禁用
- [ ] 调试模式关闭
- [ ] 错误处理配置
- [ ] 安全头配置
- [ ] CORS配置

```python
# 安全示例
# Flask安全配置
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=1800,
    WTF_CSRF_ENABLED=True
)
```

### 7.2 依赖安全
- [ ] 依赖版本管理
- [ ] 漏洞扫描
- [ ] 依赖更新
- [ ] 依赖审计
- [ ] 依赖锁定

### 7.3 安全更新
- [ ] 安全补丁
- [ ] 版本更新
- [ ] 漏洞修复
- [ ] 安全配置
- [ ] 应急响应

---

## 八、API安全

### 8.1 API认证
- [ ] API Key管理
- [ ] OAuth实现
- [ ] JWT验证
- [ ] 速率限制
- [ ] 访问控制

### 8.2 API防护
- [ ] 输入验证
- [ ] 输出过滤
- [ ] 错误处理
- [ ] 日志记录
- [ ] 监控告警

### 8.3 API设计
- [ ] 安全设计
- [ ] 最小暴露
- [ ] 版本管理
- [ ] 文档安全
- [ ] 废弃策略

---

## 九、移动端安全

### 9.1 客户端安全
- [ ] 代码混淆
- [ ] 反调试防护
- [ ] 完整性校验
- [ ] 数据加密
- [ ] 本地存储安全

### 9.2 通信安全
- [ ] 证书固定
- [ ] 双向认证
- [ ] 安全协议
- [ ] 中间人防护
- [ ] 流量加密

### 9.3 数据安全
- [ ] 本地加密
- [ ] 安全删除
- [ ] 备份安全
- [ ] 剪贴板安全
- [ ] 截图防护

---

## 十、云安全

### 10.1 身份管理
- [ ] IAM配置
- [ ] 最小权限
- [ ] 多因素认证
- [ ] 密钥管理
- [ ] 访问审计

### 10.2 数据安全
- [ ] 存储加密
- [ ] 传输加密
- [ ] 备份安全
- [ ] 访问控制
- [ ] 数据分类

### 10.3 基础设施安全
- [ ] 网络配置
- [ ] 安全组
- [ ] 防火墙
- [ ] 监控告警
- [ ] 合规检查

---

## 附录：安全检查工具

### 静态分析工具
- **通用：** SonarQube, Checkmarx
- **Python：** Bandit, Safety
- **JavaScript：** ESLint Security, npm audit
- **Java：** SpotBugs, FindSecBugs

### 动态分析工具
- **Web应用：** OWASP ZAP, Burp Suite
- **API测试：** Postman, Insomnia
- **渗透测试：** Metasploit, Kali Linux

### 依赖检查工具
- **Python：** pip-audit, safety
- **JavaScript：** npm audit, snyk
- **Java：** OWASP Dependency-Check

### 容器安全工具
- **镜像扫描：** Trivy, Clair
- **运行时保护：** Falco, Sysdig
- **编排安全：** Kubernetes Security, kube-bench

---

## 安全事件响应

### 事件分类
1. **高危事件：** 数据泄露、系统入侵
2. **中危事件：** 异常访问、权限提升
3. **低危事件：** 配置错误、安全警告

### 响应流程
1. **检测：** 发现安全事件
2. **分析：** 评估影响范围
3. **遏制：** 控制事件扩散
4. **根除：** 消除安全隐患
5. **恢复：** 恢复系统功能
6. **总结：** 总结经验教训

### 应急联系人
- **安全负责人：** [姓名/联系方式]
- **技术负责人：** [姓名/联系方式]
- **法务负责人：** [姓名/联系方式]
- **公关负责人：** [姓名/联系方式]

---

*清单版本：1.0*
*最后更新：2026年9月*