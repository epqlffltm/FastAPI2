# app.py

from fastapi import FastAPI
import uvicorn
from api import router, user

app = FastAPI()
app.include_router(router)
app.include_router(user)

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