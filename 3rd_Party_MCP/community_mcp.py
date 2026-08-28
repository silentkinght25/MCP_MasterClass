from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

async def main():
    # Create a MultiServerMCPClient instance
    client = MultiServerMCPClient(
    # MCP Server Configuration JSON
    {
        "data_fetch_mcp_studio":{
            "transport": "stdio",
            "command": "uvx",
            "args": ["duckduckgo-mcp-server"]
        }
    })
    # List tools
    tools = await client.get_tools()
    print(f"Available tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())