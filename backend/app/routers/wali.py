from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Wali
from app.schemas import WaliResponse, WaliCreate, WaliUpdate
from app.database import get_session

router = APIRouter(prefix="/wali")

@router.get("/", response_model=list[WaliResponse])
async def get_all(session: AsyncSession = Depends(get_session)) -> list[Wali]:
    result = await session.scalars(select(Wali))
    return list(result.all())

@router.get("/{id}", response_model=WaliResponse)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    wali = await session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")
    return wali

@router.post("/", response_model=WaliResponse)
async def create(payload: WaliCreate, session: AsyncSession = Depends(get_session)):
    """Create wali"""
    wali = Wali(**payload.model_dump())
    session.add(wali)
    await session.commit()
    await session.refresh(wali)
    return wali

@router.patch("/{id}", response_model=WaliResponse)
async def modify(id: int, payload: WaliUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify wali"""
    wali = await session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(wali, key, val)

    await session.commit()
    await session.refresh(wali)
    return wali

@router.delete("/{id}", response_model=WaliResponse)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    wali = await session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")

    await session.delete(wali)
    await session.commit()
    return wali


