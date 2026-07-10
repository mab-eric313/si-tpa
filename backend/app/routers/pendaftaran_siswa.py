from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PendaftaranSiswa
from app.schemas import (
    PendaftaranSiswaResponse, PendaftaranSiswaCreate, PendaftaranSiswaUpdate,
    PendaftaranSiswaRelatRes
)
from app.database import get_session
from app.dependencies import allow_admin
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/pendaftaran-siswa")

dependencies = [Depends(allow_admin)]

@router.get("/", response_model=list[PendaftaranSiswaRelatRes], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PendaftaranSiswa]:
    result = await session.scalars(
        select(PendaftaranSiswa)
        .options(selectinload(PendaftaranSiswa.kelas))
    )
    if not result:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")
    return list(result.all())

@router.get("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PendaftaranSiswa)
        .options(selectinload(PendaftaranSiswa.kelas))
        .where(PendaftaranSiswa.id == id)
    )
    pendaftaran_siswa = result.first()
    if not pendaftaran_siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")
    return pendaftaran_siswa

@router.post("/", response_model=PendaftaranSiswaResponse)
async def create(payload: PendaftaranSiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create siswa"""
    siswa = PendaftaranSiswa(**payload.model_dump())
    session.add(siswa)
    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.patch("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def modify(id: int, payload: PendaftaranSiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify siswa"""
    siswa = await session.get(PendaftaranSiswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(siswa, key, val)

    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.delete("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    siswa = await session.get(PendaftaranSiswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")

    await session.delete(siswa)
    await session.commit()
    return siswa
