from fastmcp import FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch_http():
    '''Simulates fetching data from a database or an external API.'''
    return {"data": "Hello, MCP!"}

@mcp.tool()
def process_http(path:str):
    '''Processes the fetched data.'''
    return {"processed_data": "Data has been processed at path: "+path}

if __name__ == "__main__":
    # Run the MCP server with http transport
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)