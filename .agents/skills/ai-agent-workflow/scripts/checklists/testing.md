# 测试验证检查清单

## 使用说明

本清单用于测试验证，帮助确保代码质量和功能正确性。请在测试过程中逐项检查。

---

## 一、测试准备

### 1.1 测试环境
- [ ] 测试环境配置正确
- [ ] 测试数据准备完成
- [ ] 测试工具安装配置
- [ ] 测试依赖安装
- [ ] 测试环境隔离

### 1.2 测试计划
- [ ] 测试范围明确
- [ ] 测试用例设计
- [ ] 测试数据准备
- [ ] 测试时间安排
- [ ] 测试人员分配

### 1.3 测试数据
- [ ] 正常数据准备
- [ ] 边界数据准备
- [ ] 异常数据准备
- [ ] 测试数据清理
- [ ] 测试数据备份

---

## 二、单元测试

### 2.1 测试覆盖
- [ ] 核心函数测试
- [ ] 边界条件测试
- [ ] 异常情况测试
- [ ] 返回值测试
- [ ] 参数验证测试

### 2.2 测试用例
```python
# 测试用例模板
def test_function_normal():
    """测试正常情况"""
    # 准备测试数据
    input_data = "normal input"
    expected_output = "expected output"
    
    # 执行测试
    result = function_under_test(input_data)
    
    # 验证结果
    assert result == expected_output

def test_function_edge_case():
    """测试边界情况"""
    # 准备边界数据
    input_data = ""  # 空输入
    expected_output = "default output"
    
    # 执行测试
    result = function_under_test(input_data)
    
    # 验证结果
    assert result == expected_output

def test_function_exception():
    """测试异常情况"""
    # 准备异常数据
    invalid_input = None
    
    # 执行测试并验证异常
    with pytest.raises(ValueError):
        function_under_test(invalid_input)
```

### 2.3 测试质量
- [ ] 测试用例独立
- [ ] 测试用例可重复
- [ ] 测试用例明确
- [ ] 测试用例完整
- [ ] 测试用例高效

---

## 三、集成测试

### 3.1 模块集成
- [ ] 模块间接口测试
- [ ] 数据流测试
- [ ] 依赖关系测试
- [ ] 配置集成测试
- [ ] 第三方集成测试

### 3.2 API测试
```python
# API测试示例
def test_api_endpoint():
    """测试API接口"""
    
    # 准备请求数据
    url = "/api/v1/resource"
    headers = {"Authorization": "Bearer token"}
    data = {"key": "value"}
    
    # 发送请求
    response = client.post(url, json=data, headers=headers)
    
    # 验证响应
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert "data" in response.json()
```

### 3.3 数据库测试
- [ ] 数据库连接测试
- [ ] 数据操作测试
- [ ] 事务测试
- [ ] 并发测试
- [ ] 数据一致性测试

---

## 四、功能测试

### 4.1 功能验证
- [ ] 核心功能测试
- [ ] 业务流程测试
- [ ] 用户场景测试
- [ ] 边界条件测试
- [ ] 异常情况测试

### 4.2 用户场景
```python
# 用户场景测试
def test_user_registration():
    """测试用户注册场景"""
    
    # 场景1：正常注册
    result = register_user("valid_email@example.com", "valid_password")
    assert result.success is True
    
    # 场景2：重复邮箱
    result = register_user("existing_email@example.com", "valid_password")
    assert result.success is False
    assert result.error == "Email already exists"
    
    # 场景3：弱密码
    result = register_user("new_email@example.com", "weak")
    assert result.success is False
    assert result.error == "Password too weak"
```

### 4.3 业务规则
- [ ] 业务规则正确
- [ ] 流程逻辑正确
- [ ] 状态转换正确
- [ ] 数据验证正确
- [ ] 权限控制正确

---

## 五、性能测试

### 5.1 响应时间
- [ ] 接口响应时间 < 200ms
- [ ] 页面加载时间 < 3s
- [ ] 数据库查询时间 < 100ms
- [ ] 缓存命中率 > 90%
- [ ] 并发响应时间稳定

### 5.2 吞吐量
- [ ] QPS > 1000
- [ ] 并发用户数 > 500
- [ ] 数据处理能力 > 1000条/秒
- [ ] 文件上传速度 > 10MB/s
- [ ] 文件下载速度 > 50MB/s

### 5.3 资源使用
```python
# 性能测试示例
def test_performance():
    """性能测试"""
    
    import time
    import psutil
    
    # 记录开始状态
    start_time = time.time()
    start_memory = psutil.virtual_memory().percent
    
    # 执行大量操作
    for i in range(1000):
        function_under_test(test_data)
    
    # 记录结束状态
    end_time = time.time()
    end_memory = psutil.virtual_memory().percent
    
    # 验证性能
    assert end_time - start_time < 10  # 10秒内完成
    assert end_memory - start_memory < 5  # 内存增长不超过5%
```

### 5.4 稳定性
- [ ] 长时间运行稳定
- [ ] 内存无泄漏
- [ ] 连接池正常
- [ ] 资源正常释放
- [ ] 错误恢复正常

---

## 六、安全测试

### 6.1 认证测试
- [ ] 登录功能正常
- [ ] 密码加密存储
- [ ] Token安全
- [ ] 会话管理
- [ ] 登录失败处理

### 6.2 授权测试
- [ ] 权限控制正确
- [ ] 越权访问防护
- [ ] API权限验证
- [ ] 数据权限控制
- [ ] 操作权限验证

### 6.3 输入验证
- [ ] SQL注入防护
- [ ] XSS攻击防护
- [ ] CSRF攻击防护
- [ ] 命令注入防护
- [ ] 文件上传安全

### 6.4 数据安全
- [ ] 敏感数据加密
- [ ] 传输加密（TLS）
- [ ] 数据脱敏
- [ ] 日志安全
- [ ] 数据备份

---

## 七、兼容性测试

### 7.1 浏览器兼容
- [ ] Chrome兼容
- [ ] Firefox兼容
- [ ] Safari兼容
- [ ] Edge兼容
- [ ] 移动端浏览器兼容

### 7.2 操作系统兼容
- [ ] Windows兼容
- [ ] macOS兼容
- [ ] Linux兼容
- [ ] 移动端兼容

### 7.3 设备兼容
- [ ] 桌面端兼容
- [ ] 平板兼容
- [ ] 手机兼容
- [ ] 不同分辨率兼容

---

## 八、回归测试

### 8.1 功能回归
- [ ] 核心功能回归
- [ ] 重要功能回归
- [ ] 接口回归
- [ ] 数据回归
- [ ] 性能回归

### 8.2 影响范围
- [ ] 修改影响分析
- [ ] 相关模块测试
- [ ] 依赖模块测试
- [ ] 上下游测试
- [ ] 集成点测试

### 8.3 测试策略
- [ ] 冒烟测试
- [ ] 功能测试
- [ ] 性能测试
- [ ] 安全测试
- [ ] 兼容性测试

---

## 九、测试报告

### 9.1 测试结果
- [ ] 测试用例总数
- [ ] 通过用例数
- [ ] 失败用例数
- [ ] 跳过用例数
- [ ] 测试覆盖率

### 9.2 问题汇总
- [ ] 严重问题数
- [ ] 重要问题数
- [ ] 一般问题数
- [ ] 建议问题数
- [ ] 问题修复率

### 9.3 测试结论
- [ ] 测试是否通过
- [ ] 是否可以上线
- [ ] 遗留问题说明
- [ ] 风险提示
- [ ] 建议事项

---

## 十、测试工具

### 10.1 单元测试
- **Python：** pytest, unittest
- **JavaScript：** Jest, Mocha
- **Java：** JUnit, TestNG

### 10.2 集成测试
- **API测试：** Postman, RestAssured
- **数据库测试：** SQLAlchemy, DbUnit
- **消息队列测试：** TestContainers

### 10.3 性能测试
- **负载测试：** JMeter, Locust
- **压力测试：** wrk, ab
- **监控工具：** Prometheus, Grafana

### 10.4 安全测试
- **漏洞扫描：** OWASP ZAP, Burp Suite
- **代码审计：** SonarQube, Bandit
- **渗透测试：** Metasploit

---

## 附录：测试用例模板

### 功能测试用例
```
测试用例ID：TC001
测试用例名称：用户注册功能测试
测试优先级：高
测试前置条件：用户未注册

测试步骤：
1. 打开注册页面
2. 输入有效邮箱
3. 输入有效密码
4. 点击注册按钮

预期结果：
- 注册成功
- 跳转到登录页面
- 显示成功提示

实际结果：[填写]
测试状态：[通过/失败]
测试人员：[填写]
测试日期：[填写]
```

### 接口测试用例
```
测试用例ID：TC002
测试用例名称：用户登录接口测试
测试优先级：高
测试前置条件：用户已注册

测试步骤：
1. 发送POST请求到/api/auth/login
2. 请求体：{"email": "test@example.com", "password": "password123"}
3. 验证响应

预期结果：
- 状态码：200
- 响应体：{"code": 200, "data": {"token": "..."}, "message": "success"}

实际结果：[填写]
测试状态：[通过/失败]
测试人员：[填写]
测试日期：[填写]
```

---

*清单版本：1.0*
*最后更新：2026年9月*