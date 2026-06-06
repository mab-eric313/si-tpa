"""Initialize Mariadb database"""

# TODO: (HIGH) Use asyncio
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

DB_URL = f"mariadb+mariadbconnector://" \
         f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine: Engine = create_engine(DB_URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_session():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
