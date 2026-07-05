from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PenilaianSurat
from app.schemas import PenilaianSuratResponse, PenilaianSuratCreate, PenilaianSuratUpdate
from app.database import get_session
from app.dependencies import allow_pengajar
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/penilaian-surat")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[PenilaianSuratResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PenilaianSurat]:
    result = await session.scalars(
        select(PenilaianSurat)
        .options(selectinload(PenilaianSurat.siswa))
    )
    return list(result.all())

@router.get("/{id}", response_model=PenilaianSuratResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianSurat)
        .options(selectinload(PenilaianSurat.siswa))
        .where(PenilaianSurat.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianSurat tidak ditemukan")
    return penilaian

@router.post("/", response_model=PenilaianSuratResponse, dependencies=dependencies)
async def create(payload: PenilaianSuratCreate, session: AsyncSession = Depends(get_session)):
    """Create Penilaian Surat"""
    penilaian = PenilaianSurat(**payload.model_dump())
    session.add(penilaian)
    await session.commit()
    result = await session.scalars(
        select(PenilaianSurat)
        .options(selectinload(PenilaianSurat.siswa))
        .where(PenilaianSurat.id == penilaian.id)
    )
    return result.one()

@router.patch("/{id}", response_model=PenilaianSuratResponse, dependencies=dependencies)
async def modify(id: int, payload: PenilaianSuratUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    penilaian = await session.get(PenilaianSurat, id)
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianSurat tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(penilaian, key, val)

    await session.commit()
    result = await session.scalars(
        select(PenilaianSurat)
        .options(selectinload(PenilaianSurat.siswa))
        .where(PenilaianSurat.id == penilaian.id)
    )
    return result.one()

@router.delete("/{id}", response_model=PenilaianSuratResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianSurat)
        .options(selectinload(PenilaianSurat.siswa))
        .where(PenilaianSurat.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianSurat tidak ditemukan")

    await session.delete(penilaian)
    await session.commit()
    return penilaian

