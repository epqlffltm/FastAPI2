#schema/request.py

from pydantic import BaseModel

class CreateRequest(BaseModel):
    #id: int
    contents: str
    is_done: bool