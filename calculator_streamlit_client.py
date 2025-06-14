import streamlit as st
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
import os   
import boto3

# Set AWS profile to bedrockuser
os.environ['AWS_PROFILE'] = 'bedrockuser'

# Set page config
st.set_page_config(page_title="Calculator Chat", page_icon="🧮")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def create_transport():
    return streamablehttp_client("http://0.0.0.0:8080/mcp")

# Initialize MCP client and agent
@st.cache_resource
def get_client_and_tools():
    mcp_client = MCPClient(create_transport)
    with mcp_client:
        tools = mcp_client.list_tools_sync()
        return mcp_client, tools

# Get client and tools
mcp_client, tools = get_client_and_tools()

# Display chat title
st.title("🧮 Calculator Chat")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What calculation would you like to perform?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Calculating..."):
            with mcp_client:
                agent = Agent(tools=tools)
                response = agent(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# Add a sidebar with tools and instructions
with st.sidebar:
    st.header("Available Tools")
    for tool in tools:
        st.markdown(f"### {tool.tool_name}")
        st.markdown(f"**Type:** {tool.tool_type}")
        st.markdown("**Specification:**")
        st.json(tool.tool_spec)
        st.markdown("---")

    st.header("How to use")
    st.markdown("""
    You can ask the calculator to perform operations like:
    - Add numbers: "What is 5 plus 3?"
    - Subtract numbers: "Subtract 10 from 20"
    - Multiply numbers: "Multiply 6 by 7"
    - Divide numbers: "Divide 20 by 5"
    
    Just type your calculation request in natural language!
    """) 