from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PenggantiPengajar
from app.schemas import PenggantiPengajarResponse, PenggantiPengajarCreate, PenggantiPengajarUpdate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/pengganti-pengajar")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[PenggantiPengajarResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PenggantiPengajar]:
    result = await session.scalars(select(PenggantiPengajar))
    return list(result.all())

@router.get("/{id}", response_model=PenggantiPengajarResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(PenggantiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="PenggantiPengajar tidak ditemukan")
    return kelas

@router.post("/", response_model=PenggantiPengajarResponse, dependencies=dependencies)
async def create(payload: PenggantiPengajarCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = PenggantiPengajar(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=PenggantiPengajarResponse, dependencies=dependencies)
async def modify(id: int, payload: PenggantiPengajarUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(PenggantiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="PenggantiPengajar tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=PenggantiPengajarResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(PenggantiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="PenggantiPengajar tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

