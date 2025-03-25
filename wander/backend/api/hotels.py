import requests
from fastapi import APIRouter
from config import AMADEUS_API_KEY

router = APIRouter()

@router.get("/{city}")
async def get_hotels(city: str):
    """
    Fetches available hotels for a given city.
    Example: GET /hotels/London
    """
    url = f"https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode={city}&apikey={AMADEUS_API_KEY}"
    
    response = requests.get(url).json()

    if "data" not in response:
        return {"error": "No hotels found or API issue."}

    hotels = []
    for hotel in response["data"]:
        hotels.append({
            "name": hotel["name"],
            "address": hotel["address"]["lines"],
            "rating": hotel.get("rating", "N/A"),
            "amenities": hotel.get("amenities", [])
        })

    return {"city": city, "hotels": hotels}
