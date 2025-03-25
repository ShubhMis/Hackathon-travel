import requests
from fastapi import APIRouter
from config import WEATHER_API_KEY

router = APIRouter()

@router.get("/{city}")
async def get_weather(city: str):
    """
    Fetches real-time weather data using an external API (OpenWeatherMap).
    Example: GET /weather/London
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return {"error": "City not found or API issue."}

    return {
        "city": city,
        "temperature": response["main"]["temp"],
        "weather": response["weather"][0]["description"]
    }
