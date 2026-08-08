from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def main():

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python mathserver.py",
                "args": [
                    r"D:\LEARNING_HOW_TO_CODE\MCP_AWS\mathserver.py"
                ],
                "transport": "stdio",
            },

            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )


if __name__ == "__main__":
    asyncio.run(main())