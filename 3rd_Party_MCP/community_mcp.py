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
    for tool in tools:
        print(f"Tool Name: {tool.name}, Description: {tool.description}")

    # Call a tool
    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query": "What is the capital of France?"})
    print(f"Result from {fetch_tool.name}: {result}")
    
if __name__ == "__main__":
    asyncio.run(main())