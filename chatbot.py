from fastapi import APIRouter
import openai
from config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT

router = APIRouter()

openai.api_key = AZURE_OPENAI_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT
@router.post("/")
async def get_travel_recommendation(user_query: dict):
    print("Received Request:", user_query)  # Debugging line
    query_text = f"Suggest an itinerary for {user_query['days']} days in {user_query['destination']} focusing on {', '.join(user_query['interests'])}."
    
    try:
        response = openai.ChatCompletion.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "You are an AI travel assistant."},
                {"role": "user", "content": query_text}
            ],
            max_tokens=500
        )
        return {"itinerary": response["choices"][0]["message"]["content"]}

    except Exception as e:
        print("Error calling OpenAI:", str(e))  # Print error
        return {"error": "Failed to get a response from AI"}
