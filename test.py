import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 28.61,
        "longitude": 77.21,
        "current": "temperature_2m,relative_humidity_2m,weather_code"
    }
)

print(response.status_code)
print(response.json())