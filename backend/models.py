from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends
import config

DB_USER     = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD
DB_HOST     = config.DB_HOST
DB_NAME     = config.DB_NAME

DATABASE_URL = (
    f"mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:3306/{DB_NAME}"
)

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
