from fastmcp import FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch():
    '''Simulates fetching data from a database or an external API.'''
    return {"data": "Hello, MCP!"}

@mcp.tool()
def process(path:str):
    '''Processes the fetched data.'''
    return {"processed_data": "Data has been processed at path: "+path}

if __name__ == "__main__":
    # Run the MCP server with standard input/output transport
    mcp.run(transport="stdio")