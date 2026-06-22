# app.py

from fastapi import FastAPI
import uvicorn
from api.router import router

app = FastAPI()
app.include_router(router)

@app.get('/')
async def index():
    return {"hallow": "wared"}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )