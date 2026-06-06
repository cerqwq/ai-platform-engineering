"""
AI Platform Engineering - AI平台工程工具
支持内部开发者平台、自助服务、黄金路径
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIPlatformEngineeringTools:
    """
    AI平台工程工具
    支持：IDP、自助服务、黄金路径
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_idp(self, organization: str, teams: List[str]) -> Dict:
        """设计内部开发者平台"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        teams_text = ", ".join(teams)

        prompt = f"""请为{organization}设计内部开发者平台：

团队：{teams_text}

请返回JSON格式：
{{
    "capabilities": ["能力"],
    "services": ["服务"],
    "golden_paths": ["黄金路径"],
    "self_service": ["自助服务"],
    "tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"idp": content}

    def generate_service_catalog(self, services: List[Dict]) -> str:
        """生成服务目录"""
        if not self.client:
            return "LLM客户端未配置"

        services_text = json.dumps(services, ensure_ascii=False)

        prompt = f"""请生成服务目录：

{services_text}

要求：
1. 服务描述
2. API文档
3. 使用示例
4. SLA说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_golden_path(self, application_type: str, requirements: Dict) -> Dict:
        """设计黄金路径"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        req_text = json.dumps(requirements, ensure_ascii=False)

        prompt = f"""请为{application_type}设计黄金路径：

需求：{req_text}

请返回JSON格式：
{{
    "template": "模板描述",
    "tech_stack": "技术栈",
    "ci_cd": "CI/CD管道",
    "monitoring": "监控方案",
    "documentation": "文档要求"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"golden_path": content}

    def generate_developer_portal(self, teams: List[str]) -> Dict:
        """生成开发者门户"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        teams_text = ", ".join(teams)

        prompt = f"""请为{teams_text}设计开发者门户：

请返回JSON格式：
{{
    "sections": [
        {{"name": "部分", "content": "内容", "tools": ["工具"]}}
    ],
    "features": ["功能"],
    "integrations": ["集成"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"portal": content}

    def design_platform_team(self, organization: str) -> Dict:
        """设计平台团队"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{organization}设计平台团队：

请返回JSON格式：
{{
    "roles": ["角色"],
    "responsibilities": ["职责"],
    "skills": ["技能要求"],
    "processes": ["流程"],
    "kpis": ["KPI"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"team": content}

    def generate_templates(self, application_types: List[str]) -> Dict:
        """生成项目模板"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(application_types)

        prompt = f"""请为{types_text}生成项目模板：

请返回JSON格式：
{{
    "templates": [
        {{"name": "模板名", "description": "描述", "structure": "目录结构", "features": ["功能"]}}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"templates": content}


def create_tools(**kwargs) -> AIPlatformEngineeringTools:
    """创建平台工程工具"""
    return AIPlatformEngineeringTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Platform Engineering Tools")
    print()

    # 测试
    idp = tools.design_idp("科技公司", ["前端", "后端", "数据"])
    print(json.dumps(idp, ensure_ascii=False, indent=2))
