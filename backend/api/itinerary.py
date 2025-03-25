from fastapi import APIRouter, HTTPException
from azure.cosmos import CosmosClient
import uuid
from config import COSMOSDB_URL, COSMOSDB_KEY, COSMOSDB_DATABASE, COSMOSDB_CONTAINER

router = APIRouter()

# Initialize CosmosDB Client
client = CosmosClient(COSMOSDB_URL, COSMOSDB_KEY)
database = client.get_database_client(COSMOSDB_DATABASE)
container = database.get_container_client(COSMOSDB_CONTAINER)

@router.post("/")
async def save_itinerary(itinerary: dict):
    """
    Saves a user's travel itinerary to Azure CosmosDB.
    Example Body:
    {
        "user": "john_doe",
        "destination": "Paris",
        "days": 5,
        "activities": ["Eiffel Tower", "Louvre Museum"]
    }
    """
    itinerary["id"] = str(uuid.uuid4())  # Generate a unique ID

    try:
        container.create_item(itinerary)
        return {"message": "Itinerary saved successfully!", "itinerary_id": itinerary["id"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user}")
async def get_user_itineraries(user: str):
    """
    Fetches saved itineraries for a user.
    Example: GET /itinerary/john_doe
    """
    query = f"SELECT * FROM c WHERE c.user = '{user}'"
    results = list(container.query_items(query, enable_cross_partition_query=True))

    if not results:
        return {"message": "No itineraries found for this user."}

    return {"user": user, "itineraries": results}
