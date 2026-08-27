import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio

#Path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(__file__), "first_mcpserver.py")
print(f" MCP server script: {mcp_server_script}")

server_params=StdioServerParameters(
        command="python",
        args=[mcp_server_script],
        env={}
    )

# Create a client session to communicate with the MCP server
async def main():
    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:
            await session.initialize() 
            tools = await session.list_tools()
            print(f"Available tools: {tools}")

            # Call the fetch tool
            fetch_result = await session.call_tool("fetch")
            print(f"Fetch result: {fetch_result}")

            # Call the process tool with the fetched data
            process_result = await session.call_tool("process", arguments={"path": "path/to/data"})
            print(f"Process result: {process_result}")

if __name__ == "__main__":
    asyncio.run(main())