# weather.py
from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("Weather")

WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get current weather info using OpenWeather API"""
    if not WEATHER_API_KEY:
        return "API key not found. Please set OPENWEATHER_API_KEY in your environment."
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": WEATHER_API_KEY, "units": "metric"}

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, params=params)
            data = res.json()
            desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"The weather in {location} is {desc} with temperature {temp}°C."
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
