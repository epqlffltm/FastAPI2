#database/repository.py

from sqlalchemy import select
from sqlalchemy.orm import Session
from database.orm import Data
from typing import List

def get_all_data(session:Session)-> List[Data]:
    return list(session.scalars(select(Data)))

def get_data_by_id(session: Session, id:int) -> Data | None:
    return session.scalar(select(Data).where(Data.id == id))