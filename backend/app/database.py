"""Initialize Mariadb database"""

import os
from typing import AsyncIterator
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine, 
    AsyncSession, 
    async_sessionmaker, 
    create_async_engine
)

from config import connect_args

async def create_db_if_not_exists(base_db_url: str, db_name: str | None):
    # NOTE: set echo=False when the project is ready for production
    temp_engine = create_async_engine(
        base_db_url, 
        echo=False,
        connect_args=connect_args
    )
    async with temp_engine.connect() as conn:
        await conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}`"))
        await conn.commit()

    await temp_engine.dispose()

DB_URL = os.environ["DB_URL"]

# NOTE: set echo=False when the project is ready for production
engine: AsyncEngine = create_async_engine(
    DB_URL, 
    echo=False,
    connect_args=connect_args
)

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
