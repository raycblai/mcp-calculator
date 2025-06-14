# MCP Calculator Example

This repository contains a simple calculator implementation using the Model Context Protocol (MCP).

## Files

- `calculator_mcp.py`: MCP server implementation for calculator operations
- `calculator_strand_client.py`: Client that connects to the MCP server using Strands

## Setup

1. Create a virtual environment:
```bash
python -m venv calculator_env
source calculator_env/bin/activate  # On Windows: calculator_env\Scripts\activate
```

2. Install dependencies:
```bash
pip install mcp strands boto3
```

3. Configure AWS credentials for Bedrock access in ~/.aws/credentials with a profile named "bedrockuser"

## Usage

1. Start the MCP server:
```bash
python calculator_mcp.py
```

2. In another terminal, run the client:
```bash
python calculator_strand_client.py
```

The client will connect to the MCP server and perform a calculation (2 + 3 + 4).
