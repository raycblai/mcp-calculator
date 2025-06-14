# MCP Calculator Example

This repository contains a simple calculator implementation using the Model Context Protocol (MCP).

## Files

- `calculator_mcp.py`: MCP server implementation for calculator operations
- `calculator_strand_client.py`: Command-line client that connects to the MCP server using Strands
- `calculator_streamlit_client.py`: Web interface client that provides a chat-based UI for the calculator

## Setup

1. Create a virtual environment:
```bash
python -m venv calculator_env
source calculator_env/bin/activate  # On Windows: calculator_env\Scripts\activate
```

2. Install dependencies:
```bash
pip install mcp strands boto3 streamlit
```

3. Configure AWS credentials for Bedrock access in ~/.aws/credentials with a profile named "bedrockuser"

## Usage

1. Start the MCP server:
```bash
python calculator_mcp.py
```

2. Choose one of the client options:

   a. Command-line client (simple, one-time calculation):
   ```bash
   python calculator_strand_client.py
   ```
   This will connect to the MCP server and perform a calculation (2 + 3 + 4).

   b. Streamlit web interface (interactive chat experience):
   ```bash
   streamlit run calculator_streamlit_client.py
   ```
   This will start a web server and open a browser window with a chat interface where you can enter multiple calculations.

## Web Interface Features

The Streamlit web interface provides:
- A chat-based UI for entering calculations in natural language
- History of previous calculations and results
- Instructions sidebar with example queries
- Real-time calculation processing

## How It Works

1. The MCP server exposes calculator operations as tools
2. The clients connect to the server and use these tools
3. Natural language requests are processed by the LLM (Amazon Bedrock)
4. The LLM uses the calculator tools to perform operations
5. Results are returned to the client and displayed to the user
