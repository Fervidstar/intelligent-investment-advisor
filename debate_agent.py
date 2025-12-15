# 读取必要的库
import agentscope
from agentscope.agent import ReActAgent
from agentscope.formatter import DeepSeekChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
from agentscope.mcp import HttpStatelessClient
from agentscope.tool import Toolkit, execute_python_code
from agentscope.plan import PlanNotebook, Plan, SubTask
import chat_model
from dotenv import load_dotenv, find_dotenv
import os
import asyncio

# 加载环境变量
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# 注册阿里云百炼联网搜索MCP
search_mcp=HttpStatelessClient(
    name='TongyiWebSearch',
    transport='sse',
    url='https://dashscope.aliyuncs.com/api/v1/mcps/WebSearch/sse',
    headers={
        'Authorization': f'Bearer {os.environ.get("DASHSCOPE_API_KEY")}'
    }
)

async def register_search_tool(toolkit:Toolkit)->Toolkit:
    # 注册搜索工具
    await toolkit.register_mcp_client(search_mcp)
    print("注册的 MCP 工具总数：", len(toolkit.get_json_schemas()))
    return toolkit


def debate_agent(name:str,sys_prompt:str):
    # 创建工具包
    toolkit = Toolkit()
    # 注册辩论skill
    toolkit.register_agent_skill("debate skill")
    # 注册搜索工具
    toolkit = asyncio.run(register_search_tool(toolkit))

    # 创建智能体
    return ReActAgent(
        name=name,
        model=chat_model.chat_model,
        toolkit=toolkit,
        formatter=DeepSeekChatFormatter(),
        sys_prompt=sys_prompt,
        max_iters=15,
        memory=InMemoryMemory(),
        plan_notebook=PlanNotebook(),
    )

if __name__ == "__main__":
    debate_agent('test', 'test')