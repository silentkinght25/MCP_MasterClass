from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

# Path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CH-1_CreateMCP", "first_mcpserver.py")

# Path to the Python executable in the virtual environment
python_executable = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".venv", "Scripts", "python.exe")

async def main():
    # Create a MultiServerMCPClient instance
    client = MultiServerMCPClient(

    # MCP Server Configuration JSON
    {
        "data_fetch_mcp_studio":{
            "transport": "stdio",
            "command": str(python_executable),
            "args": [str(mcp_server_script)]
        },

        "data_fetch_mcp_http":{
            "transport": "streamable-http",
            "url": "http://localhost:8050/mcp"
        }
    }
    )

    # List tools
    tools = await client.get_tools()
    print(f"Available tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())