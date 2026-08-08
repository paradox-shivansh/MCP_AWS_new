# import requests


# def get_weather(location: str) -> str:
#     # Find the location's coordinates
#     geo_response = requests.get(
#         "https://geocoding-api.open-meteo.com/v1/search",
#         params={
#             "name": location,
#             "count": 1,
#             "language": "en",
#             "format": "json"
#         }
#     )

#     geo_data = geo_response.json()

#     if "results" not in geo_data:
#         return f"Could not find location: {location}"

#     place = geo_data["results"][0]

#     latitude = place["latitude"]
#     longitude = place["longitude"]

#     # Get current weather
#     weather_response = requests.get(
#         "https://api.open-meteo.com/v1/forecast",
#         params={
#             "latitude": latitude,
#             "longitude": longitude,
#             "current": "temperature_2m,relative_humidity_2m,weather_code",
#             "timezone": "auto"
#         }
#     )

#     weather_data = weather_response.json()
#     current = weather_data["current"]

#     return (
#         f"Weather in {place['name']}:\n"
#         f"Temperature: {current['temperature_2m']}°C\n"
#         f"Humidity: {current['relative_humidity_2m']}%\n"
#         f"Weather code: {current['weather_code']}"
#     )


# def main():
#     print("Hello from mcp-aws!")
#     print(get_weather("Delhi"))


# if __name__ == "__main__":
#     main()



from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:  
    """summary
    weater for a given location"""
    
    return f"its always sunny in {location}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    
    # Transport is the method used for communication between the MCP client and your MCP server.
    # streable-http is a transport that allows for streaming responses, which is useful for long-running tasks or when you want to send partial results back to the client as they become available.