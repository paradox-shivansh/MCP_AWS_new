# from langchain_mcp_adapters.client import MCPClient
from mcp.server.fastmcp import FastMCP
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
import os
load_dotenv()

import asyncio

async def main():
    client =  MultiServerMCPClient(
        # pass
    )
