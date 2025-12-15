from agentscope.model import OpenAIChatModel, ChatResponse
from agentscope.message import Msg
from dotenv import load_dotenv, find_dotenv
import os
import asyncio

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

chat_model=OpenAIChatModel(
    model_name='deepseek-chat',
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    stream=True,
    client_kwargs={
        'base_url':'https://api.deepseek.com/v1'
    },
    generate_kwargs={
        "temperature":1.3,
        "max_tokens":8192
    }
)

reasoning_model=OpenAIChatModel(
    model_name='deepseek-reasoner',
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    client_kwargs={
        'base_url':'https://api.deepseek.com/v1'
    },
    stream=True,
    generate_kwargs={
        "temperature":1.3,
        "max_tokens":65536
    }
)

if __name__ == "__main__":
    async def test():
        res=await chat_model(
            messages=[
                {'role':'user', 'content': '你好'}
            ]
        )
        print(res)
    asyncio.run(test())