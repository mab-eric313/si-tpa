"""Initialize Mariadb database"""

import os
from typing import AsyncIterator
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncEngine, 
    AsyncSession, 
    async_sessionmaker, 
    create_async_engine
)

DB_URL = os.environ["DB_URL"]

# NOTE: set echo=False when the project is ready for production
engine: AsyncEngine = create_async_engine(DB_URL, echo=True)

Session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with Session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
