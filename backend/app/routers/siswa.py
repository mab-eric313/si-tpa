from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Siswa
from app.schemas import SiswaResponse, SiswaCreate, SiswaUpdate
from app.database import get_session

router = APIRouter(prefix="/siswa")

@router.get("/", response_model=list[SiswaResponse])
async def get_all(session: AsyncSession = Depends(get_session)) -> list[Siswa]:
    result = await session.scalars(select(Siswa))
    return list(result.all())

@router.get("/{id}", response_model=SiswaResponse)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    siswa = await session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    return siswa

@router.post("/", response_model=SiswaResponse)
async def create(payload: SiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create siswa"""
    siswa = Siswa(**payload.model_dump())
    session.add(siswa)
    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.patch("/{id}", response_model=SiswaResponse)
async def modify(id: int, payload: SiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify siswa"""
    siswa = await session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(siswa, key, val)

    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.delete("/{id}", response_model=SiswaResponse)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    siswa = await session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    await session.delete(siswa)
    await session.commit()
    return siswa
