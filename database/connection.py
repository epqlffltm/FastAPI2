#database/connection.py

from sqlalchemy import create_engine#, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL="mysql+pymysql://root:1123@127.0.0.1:3306/DATA"

engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM data"))
    for row in result:
        print(row)
        '''
        
def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()