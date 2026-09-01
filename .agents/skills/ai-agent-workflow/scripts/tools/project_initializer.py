#!/usr/bin/env python3
"""
AI智能体5级用法工作流 - 项目初始化工具

自动创建项目结构、配置文件和基础代码。
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProjectConfig:
    """项目配置数据类"""
    project_name: str
    project_type: str  # web, api, library, cli
    language: str  # python, javascript, typescript
    framework: str  # flask, django, fastapi, express, react, vue
    database: str  # none, mysql, postgresql, mongodb, redis
    features: List[str]  # auth, cache, queue, monitoring


class ProjectInitializer:
    """项目初始化器"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
    
    def create_project_structure(self, config: ProjectConfig) -> bool:
        """创建项目结构"""
        try:
            project_dir = self.project_root / config.project_name
            
            # 创建主目录
            project_dir.mkdir(exist_ok=True)
            
            # 根据项目类型创建目录结构
            if config.project_type == "web":
                self._create_web_structure(project_dir, config)
            elif config.project_type == "api":
                self._create_api_structure(project_dir, config)
            elif config.project_type == "library":
                self._create_library_structure(project_dir, config)
            elif config.project_type == "cli":
                self._create_cli_structure(project_dir, config)
            
            # 创建配置文件
            self._create_config_files(project_dir, config)
            
            # 创建文档
            self._create_documentation(project_dir, config)
            
            # 创建测试结构
            self._create_test_structure(project_dir, config)
            
            # 创建CI/CD配置
            self._create_cicd_config(project_dir, config)
            
            print(f"✅ 项目 '{config.project_name}' 创建成功!")
            print(f"📁 项目目录: {project_dir}")
            
            return True
            
        except Exception as e:
            print(f"❌ 项目创建失败: {str(e)}")
            return False
    
    def _create_web_structure(self, project_dir: Path, config: ProjectConfig):
        """创建Web项目结构"""
        # 创建目录
        dirs = [
            "src",
            "src/components",
            "src/pages",
            "src/styles",
            "src/utils",
            "public",
            "public/images",
            "public/fonts",
            "tests",
            "docs",
        ]
        
        for d in dirs:
            (project_dir / d).mkdir(parents=True, exist_ok=True)
        
        # 创建基础文件
        files = {
            "src/index.js": self._get_web_index_js(config),
            "src/App.js": self._get_web_app_js(config),
            "src/styles/main.css": self._get_main_css(config),
            "public/index.html": self._get_public_index_html(config),
            "package.json": self._get_package_json(config),
            ".gitignore": self._get_gitignore(config),
            "README.md": self._get_readme(config),
        }
        
        for file_path, content in files.items():
            (project_dir / file_path).write_text(content, encoding='utf-8')
    
    def _create_api_structure(self, project_dir: Path, config: ProjectConfig):
        """创建API项目结构"""
        # 创建目录
        dirs = [
            "src",
            "src/api",
            "src/models",
            "src/services",
            "src/utils",
            "src/config",
            "tests",
            "tests/unit",
            "tests/integration",
            "docs",
        ]
        
        for d in dirs:
            (project_dir / d).mkdir(parents=True, exist_ok=True)
        
        # 创建基础文件
        files = {
            "src/main.py": self._get_api_main_py(config),
            "src/api/__init__.py": "",
            "src/api/routes.py": self._get_api_routes_py(config),
            "src/models/__init__.py": "",
            "src/services/__init__.py": "",
            "src/utils/__init__.py": "",
            "src/config/__init__.py": self._get_config_init_py(config),
            "requirements.txt": self._get_requirements_txt(config),
            ".env.example": self._get_env_example(config),
            ".gitignore": self._get_gitignore(config),
            "README.md": self._get_readme(config),
        }
        
        for file_path, content in files.items():
            (project_dir / file_path).write_text(content, encoding='utf-8')
    
    def _create_library_structure(self, project_dir: Path, config: ProjectConfig):
        """创建库项目结构"""
        # 创建目录
        dirs = [
            "src",
            "src/lib",
            "tests",
            "docs",
            "examples",
        ]
        
        for d in dirs:
            (project_dir / d).mkdir(parents=True, exist_ok=True)
        
        # 创建基础文件
        files = {
            "src/lib/__init__.py": self._get_library_init_py(config),
            "src/lib/core.py": self._get_library_core_py(config),
            "tests/test_core.py": self._get_library_test_py(config),
            "setup.py": self._get_setup_py(config),
            "pyproject.toml": self._get_pyproject_toml(config),
            ".gitignore": self._get_gitignore(config),
            "README.md": self._get_readme(config),
        }
        
        for file_path, content in files.items():
            (project_dir / file_path).write_text(content, encoding='utf-8')
    
    def _create_cli_structure(self, project_dir: Path, config: ProjectConfig):
        """创建CLI项目结构"""
        # 创建目录
        dirs = [
            "src",
            "src/commands",
            "src/utils",
            "tests",
            "docs",
        ]
        
        for d in dirs:
            (project_dir / d).mkdir(parents=True, exist_ok=True)
        
        # 创建基础文件
        files = {
            "src/main.py": self._get_cli_main_py(config),
            "src/commands/__init__.py": "",
            "src/utils/__init__.py": "",
            "setup.py": self._get_setup_py(config),
            ".gitignore": self._get_gitignore(config),
            "README.md": self._get_readme(config),
        }
        
        for file_path, content in files.items():
            (project_dir / file_path).write_text(content, encoding='utf-8')
    
    def _create_config_files(self, project_dir: Path, config: ProjectConfig):
        """创建配置文件"""
        # 创建.editorconfig
        editorconfig = """
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4

[*.{js,ts,jsx,tsx}]
indent_size = 2

[*.{json,yml,yaml}]
indent_size = 2
"""
        (project_dir / ".editorconfig").write_text(editorconfig, encoding='utf-8')
        
        # 创建.vscode/settings.json
        vscode_dir = project_dir / ".vscode"
        vscode_dir.mkdir(exist_ok=True)
        
        settings = {
            "editor.formatOnSave": True,
            "editor.defaultFormatter": "esbenp.prettier-vscode",
            "editor.codeActionsOnSave": {
                "source.fixAll.eslint": True
            },
            "python.testing.pytestEnabled": True,
            "python.testing.unittestEnabled": False,
        }
        
        (vscode_dir / "settings.json").write_text(
            json.dumps(settings, indent=2),
            encoding='utf-8'
        )
    
    def _create_documentation(self, project_dir: Path, config: ProjectConfig):
        """创建文档"""
        docs_dir = project_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        # 创建API文档模板
        api_docs = f"""
# {config.project_name} API文档

## 概述

本文档描述了{config.project_name}项目的API接口。

## 认证

所有API请求需要在Header中包含认证信息：

```
Authorization: Bearer <token>
```

## 错误处理

所有API错误响应格式：

```json
{{
  "code": 400,
  "message": "错误描述",
  "details": "详细信息"
}}
```

## API列表

### 用户相关

#### 创建用户

- **URL:** POST /api/users
- **描述:** 创建新用户
- **请求体:**
  ```json
  {{
    "username": "string",
    "email": "string",
    "password": "string"
  }}
  ```
- **响应:**
  ```json
  {{
    "code": 200,
    "data": {{
      "id": "integer",
      "username": "string",
      "email": "string"
    }}
  }}
  ```
"""
        (docs_dir / "api.md").write_text(api_docs, encoding='utf-8')
        
        # 创建部署文档
        deploy_docs = f"""
# {config.project_name} 部署文档

## 环境要求

- Python 3.8+
- Node.js 16+ (如果是前端项目)
- Docker (可选)

## 本地开发

### 安装依赖

```bash
# Python项目
pip install -r requirements.txt

# JavaScript项目
npm install
```

### 启动开发服务器

```bash
# Python项目
python src/main.py

# JavaScript项目
npm start
```

## 生产部署

### 使用Docker

```bash
# 构建镜像
docker build -t {config.project_name} .

# 运行容器
docker run -p 8000:8000 {config.project_name}
```

### 手动部署

1. 安装依赖
2. 配置环境变量
3. 启动应用

## 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| DEBUG | 调试模式 | False |
| SECRET_KEY | 密钥 | - |
| DATABASE_URL | 数据库连接 | - |
"""
        (docs_dir / "deploy.md").write_text(deploy_docs, encoding='utf-8')
    
    def _create_test_structure(self, project_dir: Path, config: ProjectConfig):
        """创建测试结构"""
        tests_dir = project_dir / "tests"
        tests_dir.mkdir(exist_ok=True)
        
        # 创建conftest.py
        if config.language == "python":
            conftest_content = """
import pytest
from pathlib import Path


@pytest.fixture
def sample_data():
    """示例数据fixture"""
    return {
        "name": "test",
        "value": 123
    }


@pytest.fixture
def temp_dir(tmp_path):
    """临时目录fixture"""
    return tmp_path
"""
            (tests_dir / "conftest.py").write_text(conftest_content, encoding='utf-8')
            
            # 创建示例测试文件
            test_content = f"""
import pytest
from src.main import app


class TestApp:
    """应用测试类"""
    
    def test_app_exists(self):
        """测试应用是否存在"""
        assert app is not None
    
    def test_index_route(self):
        """测试首页路由"""
        # 这里添加具体的测试用例
        pass
"""
            (tests_dir / "test_app.py").write_text(test_content, encoding='utf-8')
    
    def _create_cicd_config(self, project_dir: Path, config: ProjectConfig):
        """创建CI/CD配置"""
        # 创建GitHub Actions配置
        github_dir = project_dir / ".github" / "workflows"
        github_dir.mkdir(parents=True, exist_ok=True)
        
        workflow_content = f"""
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/ -v
    
    - name: Run linting
      run: |
        python -m flake8 src/
        python -m black --check src/
"""
        (github_dir / "ci.yml").write_text(workflow_content, encoding='utf-8')
    
    def _get_web_index_js(self, config: ProjectConfig) -> str:
        """获取Web index.js内容"""
        return f"""
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/main.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""
    
    def _get_web_app_js(self, config: ProjectConfig) -> str:
        """获取Web App.js内容"""
        return f"""
import React from 'react';

function App() {{
  return (
    <div className="App">
      <header className="App-header">
        <h1>{config.project_name}</h1>
        <p>
          Welcome to {config.project_name}
        </p>
      </header>
    </div>
  );
}}

export default App;
"""
    
    def _get_main_css(self, config: ProjectConfig) -> str:
        """获取主CSS内容"""
        return f"""
/* {config.project_name} 主样式 */

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}}

.App {{
  text-align: center;
}}

.App-header {{
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}}
"""
    
    def _get_public_index_html(self, config: ProjectConfig) -> str:
        """获取public index.html内容"""
        return f"""
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="{config.project_name} - AI智能体5级用法工作流项目" />
    <title>{config.project_name}</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
"""
    
    def _get_package_json(self, config: ProjectConfig) -> str:
        """获取package.json内容"""
        return f"""
{{
  "name": "{config.project_name}",
  "version": "1.0.0",
  "description": "{config.project_name} - AI智能体5级用法工作流项目",
  "main": "src/index.js",
  "scripts": {{
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }},
  "dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  }},
  "devDependencies": {{
    "eslint": "^8.0.0",
    "prettier": "^3.0.0"
  }},
  "browserslist": {{
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  }}
}}
"""
    
    def _get_api_main_py(self, config: ProjectConfig) -> str:
        """获取API main.py内容"""
        framework_config = {
            "flask": self._get_flask_main,
            "django": self._get_django_main,
            "fastapi": self._get_fastapi_main,
        }
        
        if config.framework in framework_config:
            return framework_config[config.framework](config)
        else:
            return self._get_flask_main(config)
    
    def _get_flask_main(self, config: ProjectConfig) -> str:
        """获取Flask main.py内容"""
        return f"""
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    \"\"\"首页\"\"\"
    return jsonify({{
        "message": "Welcome to {config.project_name}",
        "version": "1.0.0"
    }})


@app.route('/api/health')
def health_check():
    \"\"\"健康检查\"\"\"
    return jsonify({{
        "status": "healthy",
        "timestamp": "{{current_timestamp}}"
    }})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
"""
    
    def _get_django_main(self, config: ProjectConfig) -> str:
        """获取Django main.py内容"""
        return f"""
#!/usr/bin/env python
\"\"\"Django's command-line utility for administrative tasks.\"\"\"
import os
import sys


def main():
    \"\"\"Run administrative tasks.\"\"\"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{config.project_name}.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
"""
    
    def _get_fastapi_main(self, config: ProjectConfig) -> str:
        """获取FastAPI main.py内容"""
        return f"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(
    title="{config.project_name}",
    description="AI智能体5级用法工作流项目",
    version="1.0.0"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    \"\"\"首页\"\"\"
    return {{
        "message": "Welcome to {config.project_name}",
        "version": "1.0.0"
    }}


@app.get("/api/health")
async def health_check():
    \"\"\"健康检查\"\"\"
    return {{
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }}
"""
    
    def _get_api_routes_py(self, config: ProjectConfig) -> str:
        """获取API routes.py内容"""
        return f"""
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)


@api.route('/users', methods=['GET'])
def get_users():
    \"\"\"获取用户列表\"\"\"
    # TODO: 实现获取用户列表逻辑
    return jsonify({{
        "code": 200,
        "data": []
    }})


@api.route('/users', methods=['POST'])
def create_user():
    \"\"\"创建用户\"\"\"
    data = request.get_json()
    
    # TODO: 实现创建用户逻辑
    return jsonify({{
        "code": 200,
        "message": "用户创建成功"
    }})
"""
    
    def _get_config_init_py(self, config: ProjectConfig) -> str:
        """获取config __init__.py内容"""
        return f"""
import os


class Config:
    \"\"\"配置类\"\"\"
    
    # 基础配置
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # 数据库配置
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    
    # Redis配置
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
"""
    
    def _get_requirements_txt(self, config: ProjectConfig) -> str:
        """获取requirements.txt内容"""
        deps = ["flask>=2.3.0", "flask-cors>=4.0.0"]
        
        if "auth" in config.features:
            deps.extend(["flask-jwt-extended>=4.5.0", "bcrypt>=4.0.0"])
        
        if "cache" in config.features:
            deps.append("redis>=5.0.0")
        
        if "queue" in config.features:
            deps.append("celery>=5.3.0")
        
        return "\n".join(deps)
    
    def _get_env_example(self, config: ProjectConfig) -> str:
        """获取.env.example内容"""
        return f"""
# {config.project_name} 环境变量配置

# 基础配置
DEBUG=True
SECRET_KEY=your-secret-key-here

# 数据库配置
DATABASE_URL=sqlite:///app.db

# Redis配置
REDIS_URL=redis://localhost:6379/0

# JWT配置
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_EXPIRES=3600
"""
    
    def _get_gitignore(self, config: ProjectConfig) -> str:
        """获取.gitignore内容"""
        return f"""
# {config.project_name} .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
htmlcov/
.pytest_cache/
.tox/
.nox/

# Logs
*.log
logs/

# Environment
.env
.env.local
.env.*.local
"""
    
    def _get_readme(self, config: ProjectConfig) -> str:
        """获取README.md内容"""
        return f"""
# {config.project_name}

> AI智能体5级用法工作流项目

## 📋 项目概述

这是一个使用AI智能体5级用法工作流创建的{config.project_type}项目。

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+ (如果是前端项目)

### 安装依赖

```bash
# Python项目
pip install -r requirements.txt

# JavaScript项目
npm install
```

### 启动项目

```bash
# Python项目
python src/main.py

# JavaScript项目
npm start
```

## 📁 项目结构

```
{config.project_name}/
├── src/                # 源代码
├── tests/              # 测试文件
├── docs/               # 文档
├── requirements.txt    # Python依赖
├── package.json        # Node.js依赖
└── README.md           # 项目说明
```

## 🛠️ 开发指南

### 代码规范

- 使用PEP 8规范 (Python)
- 使用ESLint规范 (JavaScript)
- 使用Black格式化代码

### 测试

```bash
# 运行测试
python -m pytest tests/ -v

# 运行特定测试
python -m pytest tests/test_app.py -v
```

## 📚 文档

- [API文档](docs/api.md)
- [部署文档](docs/deploy.md)

## 🤝 贡献

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证

本项目基于MIT许可证开源。
"""


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("使用方法: python project_initializer.py <项目名称> [选项]")
        print("选项:")
        print("  --type: 项目类型 (web, api, library, cli)")
        print("  --lang: 编程语言 (python, javascript, typescript)")
        print("  --framework: 框架 (flask, django, fastapi, express, react, vue)")
        print("  --db: 数据库 (none, mysql, postgresql, mongodb, redis)")
        print("  --features: 功能 (auth, cache, queue, monitoring)")
        print("")
        print("示例:")
        print("  python project_initializer.py my-project --type api --lang python --framework fastapi")
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    # 解析参数
    config = ProjectConfig(
        project_name=project_name,
        project_type="api",
        language="python",
        framework="flask",
        database="none",
        features=[]
    )
    
    # 简单的参数解析
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--type" and i + 1 < len(sys.argv):
            config.project_type = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--lang" and i + 1 < len(sys.argv):
            config.language = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--framework" and i + 1 < len(sys.argv):
            config.framework = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--db" and i + 1 < len(sys.argv):
            config.database = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--features" and i + 1 < len(sys.argv):
            config.features = sys.argv[i + 1].split(",")
            i += 2
        else:
            i += 1
    
    # 创建项目
    initializer = ProjectInitializer()
    success = initializer.create_project_structure(config)
    
    if success:
        print("\n✅ 项目初始化完成!")
        print(f"📁 进入项目目录: cd {project_name}")
        print("🚀 开始开发吧!")
    else:
        print("\n❌ 项目初始化失败!")
        sys.exit(1)


if __name__ == "__main__":
    main()
