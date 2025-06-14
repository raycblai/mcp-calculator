from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
import boto3
import os

# Set AWS profile to bedrockuser
os.environ['AWS_PROFILE'] = 'bedrockuser'

def create_transport():
    return streamablehttp_client("http://0.0.0.0:8080/mcp")

mcp_client = MCPClient(create_transport)

with mcp_client:
    # List available tools from the MCP server
    tools = mcp_client.list_tools_sync()
    # Create an agent with these tools
    agent = Agent(tools=tools)
    # Use the agent as needed
    result = agent("2 + 3 + 4 ")
    print(result)
