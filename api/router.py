# api/router.py

from fastapi import APIRouter, Body, HTTPException, Depends
import random
from typing import List
from database.orm import Data
from schema.request import CreateRequest
from schema.response import DataSchema
from security import get_access_token
from service.user import UserService
from database.repository import DataRepository, UserRepository

router = APIRouter()

@router.get("/data", status_code=200)
async def get_datas(
    order: str | None = None, data_repo: DataRepository = Depends(),
    access_token: str = Depends(get_access_token),
    user_service: UserService= Depends(),
    user_repo: UserRepository = Depends(),
    ):
    username: str = user_service.decode_jwt(access_token=access_token)
    user: User | None = user_repo.get_user_by_username(username=username)
    if not user:
        raise HTTPException(status_code = 404, detail="user not found")
        
    data: List[Data] = data_repo.get_all_data()
    if order is None:
        return data
    order = order.upper()
    if order == "DESC":
        return data[::-1]
    elif order == 'ASC':
        return data
    else:
        return random.sample(data, len(data))

@router.get("/data/{id}", status_code=200)
async def get_data_handler(id: int, data_repo: DataRepository = Depends()) -> DataSchema:
    item: Data | None = data_repo.get_data_by_id(id=id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="id not found")

@router.post("/data/create", status_code=201)
async def create_data_handler(request: CreateRequest, data_repo: DataRepository = Depends()) -> DataSchema:
    data: Data = Data.create(request=request)
    data: Data = data_repo.create_data(data=data)
    return DataSchema.model_validate(data)

@router.patch("/data/update/{id}", status_code=200)
async def update_data_handler(id: int, is_done: bool = Body(..., embed=True), data_repo: DataRepository = Depends()) -> DataSchema:
    item: Data | None = data_repo.get_data_by_id(id=id)
    if item:
        item.done() if is_done else item.undone()
        item: Data = data_repo.update_data(data=item)
        return DataSchema.model_validate(item)
    raise HTTPException(status_code=404, detail="id not found")

@router.delete("/data/{id}", status_code=204)
async def delete_data_handler(id: int, data_repo: DataRepository = Depends()):
    item: Data | None = data_repo.get_data_by_id(id=id)
    if not item:
        raise HTTPException(status_code=404, detail="item not fount")
    data_repo.delete_data(id=id)