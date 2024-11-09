# src/server/python.py
from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI()

@app.get("/python/hello")
async def hello():
    return {"message": "Ram Ram Bhaay from Pragyan"}

@app.get("/developer")
async def developer():
    return {"Telegram username is @Pragyan"}

@app.get("/instagramvideo")
async def instagram_video(postUrl: str):
    try:
        # Forward the request to the specified API endpoint
        api_url = f"https://pragyaninstagr.vercel.app/api/video?postUrl={postUrl}"
        response = requests.get(api_url)
        
        # If the external API responds successfully, return its JSON data
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch video data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
