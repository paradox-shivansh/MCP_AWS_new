from langchain_mcp_adapters import MCPClient
from mcp.server.fastmcp import FastMCP
from langgraph.prebuilt import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

import asyncio

async def main():
    client = MultiServiceClient(
        # pass
    )
