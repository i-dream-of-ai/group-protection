from typing import Any
from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("group-protection")

def get_recent_activity_data() -> dict[str, Any] | None:
    try:
        file_path = os.path.join(os.path.dirname(__file__), "events.json")
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None
    
@mcp.tool()
async def get_recent_activity() -> str:
    """
    Get recent Group Protection activity data.
    """
    data = get_recent_activity_data()
    if data is None:
        return "No recent activity data available."
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    # Initialise and run the server
    mcp.run(transport='stdio')