from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TrgLogSiswa
from app.schemas import TrgLogSiswaResponse, TrgLogSiswaCreate, TrgLogSiswaUpdate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/trg-log-siswa")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[TrgLogSiswaResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[TrgLogSiswa]:
    result = await session.scalars(select(TrgLogSiswa))
    return list(result.all())

@router.get("/{id}", response_model=TrgLogSiswaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(TrgLogSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="TrgLogSiswa tidak ditemukan")
    return kelas

@router.post("/", response_model=TrgLogSiswaResponse, dependencies=dependencies)
async def create(payload: TrgLogSiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = TrgLogSiswa(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=TrgLogSiswaResponse, dependencies=dependencies)
async def modify(id: int, payload: TrgLogSiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(TrgLogSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="TrgLogSiswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=TrgLogSiswaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(TrgLogSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="TrgLogSiswa tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

