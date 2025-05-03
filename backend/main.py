from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agents import Agent
import uvicorn
import os

# Load API key from environment
env_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
if env_api_key:
    os.environ["ALPHAVANTAGE_API_KEY"] = env_api_key

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize your Agent
agent = Agent()

@app.post("/query")
async def query(request: Request):
    """
    Receives a JSON payload with 'messages' list and forwards it to agent.advisor.invoke.
    Example body:
    {
      "messages": [
        {"role": "user", "content": "What is the investment recommendation for AMZN?"}
      ]
    }
    """
    payload = await request.json()
    result = agent.advisor.invoke(payload)
    return {"message": result['messages'][-1].content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)