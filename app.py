# app.py

from fastapi import FastAPI,Body, HTTPException
from pydantic import BaseModel
import uvicorn,random

app = FastAPI()

@app.get('/')
async def index():
    return {"hallow" : "wared"}

data = {
    1:{"id":1, "contents":"fastapi 1", "is_done":True},
    2:{"id":2, "contents":"fastapi 2", "is_done":False},
    3:{"id":3, "contents":"fastapi 3", "is_done":False},
}

@app.get("/data", status_code=200)
async def get_datas(order:str = 'asc'):
    ret = list(data.values())
    order = order.upper()
    if order == "DESC":
        return ret[::-1]
    elif order == 'ASC':
        return ret
    else:
        return random.sample(ret, len(ret)) 
    
@app.get("/data/{id}",status_code=200)
async def get_data_handler(id:int):
    item = data.get(id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="id not found")

class CreateRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

@app.post("/data/create",status_code=201)
async def create_data(request: CreateRequest):
    data[request.id] = request
    return

@app.patch("/data/update/{id}",status_code=200)
async def update_data(id: int, is_done: bool = Body(...,embed=True)):
    item = data.get(id)
    if item:
        item["is_done"] = is_done
        return item
    raise HTTPException(status_code=404, detail="item not found")

@app.delete("/data/{id}",status_code=204)
async def delete_data(id:int):
    item = data.pop(id,None)
    if item:
        return
    raise HTTPException(status_code=404, detail="item not fount")

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )