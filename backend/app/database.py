"""Initialize Mariadb database"""

from typing import AsyncIterator
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncEngine, 
    AsyncSession, 
    async_sessionmaker, 
    create_async_engine
)
from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

DB_URL = f"mariadb+asyncmy://" \
         f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# NOTE: set echo=False when the project is ready for production
engine: AsyncEngine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()
Session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with Session() as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise
