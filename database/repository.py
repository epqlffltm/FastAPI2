# database/repository.py

from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from fastapi import Depends
from database.orm import Data
from database.connection import get_db
from typing import List

class DataRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_all_data(self) -> List[Data]:
        return list(self.session.scalars(select(Data)))

    def get_data_by_id(self, id: int) -> Data | None:
        return self.session.scalar(select(Data).where(Data.id == id))

    def create_data(self, data: Data) -> Data:
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def update_data(self, data: Data) -> Data:
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def delete_data(self, id: int) -> None:
        self.session.execute(delete(Data).where(Data.id == id))
        self.session.commit()