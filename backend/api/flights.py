import requests
from fastapi import APIRouter

router = APIRouter()

@router.get("/{airport_code}")
async def get_flights(airport_code: str):
    """
    Fetches live flight data for a given airport.
    Example: GET /flights/LAX
    """
    url = f"https://opensky-network.org/api/states/all"
    response = requests.get(url).json()

    # Extract flights matching the airport code
    matching_flights = []
    for flight in response.get("states", []):
        if flight[2] == airport_code:  # flight[2] = origin_airport
            matching_flights.append({
                "callsign": flight[1],
                "origin_airport": flight[2],
                "destination": flight[3],
                "latitude": flight[5],
                "longitude": flight[6],
                "altitude": flight[7],
                "velocity": flight[9]
            })

    if not matching_flights:
        return {"error": "No flights found for this airport."}

    return {"airport": airport_code, "flights": matching_flights}
