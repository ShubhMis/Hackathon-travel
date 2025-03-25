import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

AZURE_OPENAI_KEY = "Fj1KPt7grC6bAkNja7daZUstpP8wZTXsV6Zjr2FOxkO7wsBQ5SzQJQQJ99BCACHYHv6XJ3w3AAAAACOGL3Xg"
AZURE_OPENAI_ENDPOINT = "https://ai-aihackthonhub282549186415.openai.azure.com"
AZURE_OPENAI_DEPLOYMENT = "gpt-4"
WEATHER_API_KEY = "315f5e9a12a5c3482dc4987524e9dc02"  # Replace with your actual key

# Flight API Key (for future use)
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY", "your-flight-api-key")

# Amadeus API Key for Hotels
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY", "your-amadeus-api-key")

# Azure CosmosDB Connection
COSMOSDB_URL = os.getenv("COSMOSDB_URL", "your-cosmos-db-url")
COSMOSDB_KEY = os.getenv("COSMOSDB_KEY", "your-cosmos-db-key")
COSMOSDB_DATABASE = "travel_assistant"
COSMOSDB_CONTAINER = "itineraries"