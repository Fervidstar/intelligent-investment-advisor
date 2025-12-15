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


def Judge_agent(name:str,sys_prompt:str):
    # 创建工具包
    toolkit = Toolkit()
    # 注册主持skill
    toolkit.register_agent_skill("judge skill")

    # 创建智能体
    return ReActAgent(
        name=name,
        model=chat_model.reasoning_model,
        toolkit=toolkit,
        formatter=DeepSeekChatFormatter(),
        sys_prompt=sys_prompt,
        max_iters=3,
        memory=InMemoryMemory(),
    )

if __name__ == "__main__":
    Judge_agent('test', 'test')