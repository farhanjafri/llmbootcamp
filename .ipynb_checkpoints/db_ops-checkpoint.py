from sqlmodel import SQLModel, Field, Session, select, create_engine
#from sqlalchemy.future import create_engine
import pandas as pd

from typing import List

class Config(SQLModel, table=True):
    key: int = Field(default=None, primary_key=True)
    value: bytes
    
DATABASE_URL = "postgresql+psycopg://transformers:supportvectors.123@localhost:5432/vectordb"

engine = create_engine(DATABASE_URL)

def select_configuration():
    with Session(engine) as session:
        statement = select(configuration)
        results = session.exec(statement).all()
        for data in results:
            print("configuration:", data)
        return results

def get_configuration(model):
    data = select_configuration(model)
    return pd.DataFrame([dict(item) for item in data])

