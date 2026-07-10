from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import SppSiswa
from app.schemas import SppSiswaResponse, SppSiswaCreate, SppSiswaUpdate
from app.database import get_session
from app.dependencies import allow_pengajar
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/spp-siswa")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[SppSiswaResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[SppSiswa]:
    result = await session.scalars(
        select(SppSiswa)
        .options(selectinload(SppSiswa.siswa))
    )
    return list(result.all())

@router.get("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(SppSiswa)
        .options(selectinload(SppSiswa.siswa))
        .where(SppSiswa.id == id)
    )
    spp_siswa = result.first()
    if not spp_siswa:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")
    return spp_siswa

@router.post("/", response_model=SppSiswaResponse, dependencies=dependencies)
async def create(payload: SppSiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    spp_siswa = SppSiswa(**payload.model_dump())
    session.add(spp_siswa)
    await session.commit()

    result = await session.scalars(
        select(SppSiswa)
        .options(selectinload(SppSiswa.siswa))
        .where(SppSiswa.id == spp_siswa.id)
    )
    return result.first()

@router.patch("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def modify(id: int, payload: SppSiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    spp_siswa = await session.get(SppSiswa, id)
    if not spp_siswa:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(spp_siswa, key, val)

    await session.commit()

    result = await session.scalars(
        select(SppSiswa)
        .options(selectinload(SppSiswa.siswa))
        .where(SppSiswa.id == spp_siswa.id)
    )
    return result.one()

@router.delete("/{id}", response_model=SppSiswaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(SppSiswa)
        .options(selectinload(SppSiswa.siswa))
        .where(SppSiswa.id == id)
    )
    spp_siswa = result.first()
    if not spp_siswa:
        raise HTTPException(status_code=404, detail="SppSiswa tidak ditemukan")

    await session.delete(spp_siswa)
    await session.commit()
    return spp_siswa

