# 🏗️ AI Platform Engineering

AI平台工程工具，支持内部开发者平台、自助服务、黄金路径。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 内部开发者平台设计
- 📋 服务目录生成
- 🛤️ 黄金路径设计
- 🚪 开发者门户
- 👥 平台团队设计
- 📦 项目模板生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_platform_engineering import create_tools

tools = create_tools()

# IDP设计
idp = tools.design_idp("科技公司", ["前端", "后端", "数据"])

# 服务目录
catalog = tools.generate_service_catalog(services)

# 黄金路径
golden_path = tools.design_golden_path("Web应用", requirements)

# 开发者门户
portal = tools.generate_developer_portal(["前端", "后端"])

# 平台团队
team = tools.design_platform_team("科技公司")

# 项目模板
templates = tools.generate_templates(["Web应用", "API服务"])
```

## 📁 项目结构

```
ai-platform-engineering/
├── tools.py       # 平台工程工具核心
└── README.md
```

## 📄 许可证

MIT License
