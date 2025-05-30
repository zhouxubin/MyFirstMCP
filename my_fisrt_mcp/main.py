from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="my-first-mcp")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers
    Args:
        a: The first number
        b: The second number
    Returns:
        The sum of the two numbers
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers
    Args:
        a: The first number
        b: The second number
    Returns:
        The difference between the two numbers
    """
    return a - b

if __name__ == "__main__":
    mcp.run()