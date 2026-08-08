But the AI model doesn't automatically know:

that this function exists
what arguments it takes
what it returns
how to communicate with it
how to serialize the request
how to handle the MCP protocol

FastMCP handles much of that infrastructure for you.


# Transport is the method used for communication between the MCP client and your MCP server.

# STDIO is particularly useful when your MCP server is running locally and the MCP client launches it.


# client.py is used to connect the client to the mcp server and services of the tools you created we are using langchain_mcp adapters here

