from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """__summary__
    Add two numbers
    returns the sum of a and b"""
    return a + b


@mcp.tool()
def multiply(a:int, b:int) -> int:
    """__summary__
    Multiply two numbers
    returns the product of a and b"""
    return a * b

@mcp.tool()
def divide(a:int, b:int) -> float:
    """__summary__
    Divide two numbers
    returns the quotient of a and b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def subtract(a:int, b:int) -> int:
    """__summary__
    Subtract two numbers
    returns the difference of a and b"""
    return a - b



if __name__ == "__main__":
    mcp.run(transport="stdio")
    
    # Transport is the method used for communication between the MCP client and your MCP server.
    