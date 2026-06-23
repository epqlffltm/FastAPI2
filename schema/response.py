#schema/response.py

from pydantic import BaseModel, ConfigDict
from typing import List

class DataSchema(BaseModel):
    id: int
    contents: str
    is_done: bool
    
    model_config = ConfigDict(from_attributes=True)
    
class ListDataResponse(BaseModel):
    data:List[DataSchema]
    
class UserSchema(BaseModel):
    id: int
    username: str
    
    model_config = ConfigDict(from_attributes=True)