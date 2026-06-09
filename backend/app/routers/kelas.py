from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Kelas
from app.schemas import KelasResponse, KelasCreate, KelasUpdate
from app.database import get_session

router = APIRouter(prefix="/kelas")

@router.get("/", response_model=list[KelasResponse])
async def get_all(session: AsyncSession = Depends(get_session)) -> list[Kelas]:
    result = await session.scalars(select(Kelas))
    return list(result.all())

@router.get("/{id}", response_model=KelasResponse)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")
    return kelas

@router.post("/", response_model=KelasResponse)
async def create(payload: KelasCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = Kelas(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=KelasResponse)
async def modify(id: int, payload: KelasUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=KelasResponse)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

