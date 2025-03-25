from fastapi import FastAPI
from api.chatbot import router as chatbot_router
from api.weather import router as weather_router
from api.flights import router as flights_router
from api.hotels import router as hotels_router
from api.itinerary import router as itinerary_router

app = FastAPI(title="AI-Based Smart Travel Assistant")

# Include APIs
app.include_router(chatbot_router, prefix="/chatbot")
app.include_router(weather_router, prefix="/weather")
app.include_router(flights_router, prefix="/flights")
app.include_router(hotels_router, prefix="/hotels")
app.include_router(itinerary_router, prefix="/itinerary")

@app.get("/")
def home():
    return {"message": "Welcome to AI Smart Travel Assistant!"}
