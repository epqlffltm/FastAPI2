from app import app
from database.connection import get_db
from database.orm import Data
from database.repository import get_all_data


import random
from typing import List


@app.get("/data", status_code=200)
async def get_datas(order:str | None = None, session: Session = Depends(get_db)):

    data: List[Data] = get_all_data(session=session)

    #ret = list(data.values())
    #order = order.upper()
    if order == None:
        return data
    order = order.upper()
    if order == "DESC":
        return data[::-1]
    elif order == 'ASC':
        return data
    else:
        return random.sample(data, len(data))