import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent


load_dotenv()


async def main():

    client = MultiServerMCPClient({

        "math": {
            "command": "python",
            "args": [
                r"D:\LEARNING_HOW_TO_CODE\MCP_AWS\mathserver.py"
            ],
            "transport": "stdio",
        },

        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        },
    })

    tools = await client.get_tools()

    model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    agent = create_agent(
        model,
        tools
    )

    response = await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": "What is 25 multiplied by 4?"
            }
        ]
    })

    print(response)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())