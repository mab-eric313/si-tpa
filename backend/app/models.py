# TODO: (LOW) Is models module needed? Currently this module is not used.
# Use this when real data is ready
# or maybe this file is not required

from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends
import config

DB_URL = (f"sqlite:///{config.DB_NAME}")
connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL, connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
