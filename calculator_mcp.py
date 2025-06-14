from fastmcp import FastMCP
import os
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables from .env file
load_dotenv()

# Get environment variables with defaults
server_name = os.getenv("SERVER_NAME", "my-calculator")
server_instructions = os.getenv("SERVER_DESCRIPTION", "This is the calculation that can do add, subtract, multiply, divide")

# Create the FastMCP server instance
server = FastMCP(name=server_name, instructions=server_instructions)

@server.tool(
    name="add",
    description="Add two numbers together"
)
def add(a: float, b: float) -> Dict[str, Any]:
    """Add two numbers and return the result."""
    return {"result": a + b}

@server.tool(
    name="subtract",
    description="Subtract second number from first number"
)
def subtract(a: float, b: float) -> Dict[str, Any]:
    """Subtract b from a and return the result."""
    return {"result": a - b}

@server.tool(
    name="multiply",
    description="Multiply two numbers together"
)
def multiply(a: float, b: float) -> Dict[str, Any]:
    """Multiply two numbers and return the result."""
    return {"result": a * b}

@server.tool(
    name="divide",
    description="Divide first number by second number"
)
def divide(a: float, b: float) -> Dict[str, Any]:
    """Divide a by b and return the result with error handling for division by zero."""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return {"result": a / b}
    except ZeroDivisionError as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Run the server using environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))
    server.run(transport="streamable-http", host=host, port=port)
