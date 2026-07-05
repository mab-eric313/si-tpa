from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import BiodataUser
from app.schemas import BiodataUserResponse, BiodataUserCreate, BiodataUserUpdate
from app.database import get_session
from app.dependencies import allow_admin

router = APIRouter(prefix="/biodata-user")

dependencies = [Depends(allow_admin)]

@router.get("/", response_model=list[BiodataUserResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[BiodataUser]:
    result = await session.scalars(select(BiodataUser))
    return list(result.all())

@router.get("/{id}", response_model=BiodataUserResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")
    return kelas

@router.post("/", response_model=BiodataUserResponse, dependencies=dependencies)
async def create(payload: BiodataUserCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = BiodataUser(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=BiodataUserResponse, dependencies=dependencies)
async def modify(id: int, payload: BiodataUserUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=BiodataUserResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

