from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import GajiPengajar
from app.schemas import GajiPengajarResponse, GajiPengajarCreate, GajiPengajarUpdate
from app.database import get_session
from app.dependencies import allow_admin

router = APIRouter(prefix="/gaji-pengajar")

dependencies = [Depends(allow_admin)]

@router.get("/", response_model=list[GajiPengajarResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[GajiPengajar]:
    result = await session.scalars(select(GajiPengajar))
    return list(result.all())

@router.get("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(GajiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")
    return kelas

@router.post("/", response_model=GajiPengajarResponse, dependencies=dependencies)
async def create(payload: GajiPengajarCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = GajiPengajar(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def modify(id: int, payload: GajiPengajarUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(GajiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(GajiPengajar, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

