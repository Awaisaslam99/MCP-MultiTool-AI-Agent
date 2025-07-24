# search_tool.py
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
import wikipedia

mcp = FastMCP("Search")

@mcp.tool()
def search_duckduckgo(query: str) -> str:
    """Answer recent or factual questions using DuckDuckGo search."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if not results:
                return "No relevant results found."
            return "\n\n".join(f"- {res['title']}: {res['body']}" for res in results)
    except Exception as e:
        return f"Error during DuckDuckGo search: {str(e)}"

@mcp.tool()
def wikipedia_summary(query: str) -> str:
    """Get a short summary from Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except Exception as e:
        return f"Error fetching Wikipedia summary: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
