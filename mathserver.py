from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiple(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract second number from first"""
    return a - b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide first number by second"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def power(base: int, exponent: int) -> int:
    """Raise base to the power of exponent"""
    return base ** exponent

@mcp.tool()
def modulus(a: int, b: int) -> int:
    """Return the remainder when a is divided by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b

@mcp.tool()
def absolute(n: int) -> int:
    """Return the absolute value of a number"""
    return abs(n)

@mcp.tool()
def max_of_two(a: int, b: int) -> int:
    """Return the maximum of two numbers"""
    return max(a, b)

if __name__ == "__main__":
    mcp.run(transport="stdio")
