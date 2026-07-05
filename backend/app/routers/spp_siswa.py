from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import SppSiswa
from app.schemas import SppSiswaResponse, SppSiswaCreate, SppSiswaUpdate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/spp-siswa")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[SppSiswaResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[SppSiswa]:
    result = await session.scalars(select(SppSiswa))
    return list(result.all())

@router.get("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(SppSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")
    return kelas

@router.post("/", response_model=SppSiswaResponse, dependencies=dependencies)
async def create(payload: SppSiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = SppSiswa(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def modify(id: int, payload: SppSiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(SppSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(SppSiswa, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

