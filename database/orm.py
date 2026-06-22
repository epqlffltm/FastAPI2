#database/orm.py

from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
from schema.request import CreateRequest

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    
    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)
    
    def __repr__(self):
        return f"data(id = {self.id}, contents={self.contents}, is_done = {self.is_done})"
    
    @classmethod
    def create(cls, request: CreateRequest) -> "Data":
        return cls(
            contents=request.contents,
            is_done=request.is_done
        )
        
    def done(self) -> "Data":
        self.is_done = True
        return self
        
    def undone(self) -> "Data":
        self.is_done = False
        return self