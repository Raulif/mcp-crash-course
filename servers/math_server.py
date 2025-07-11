# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("<ADD> ", "a: ", a, "b: ", b)
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("<MULTIPLY> ", "a: ", a, "b: ", b)
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
