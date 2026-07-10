from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import GajiPengajar
from app.schemas import GajiPengajarResponse, GajiPengajarCreate, GajiPengajarUpdate
from app.database import get_session
from app.dependencies import allow_admin

router = APIRouter(prefix="/gaji-pengajar")

dependencies = [Depends(allow_admin)]

@router.get("/", response_model=list[GajiPengajarResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[GajiPengajar]:
    result = await session.scalars(
        select(GajiPengajar)
        .options(selectinload(GajiPengajar.biodata_user))
    )
    return list(result.all())

@router.get("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(GajiPengajar)
        .options(selectinload(GajiPengajar.biodata_user))
        .where(GajiPengajar.id == id)
    )
    gaji_pengajar = result.first()
    if not gaji_pengajar:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")
    return gaji_pengajar

@router.post("/", response_model=GajiPengajarResponse, dependencies=dependencies)
async def create(payload: GajiPengajarCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    gaji_pengajar = GajiPengajar(**payload.model_dump())
    session.add(gaji_pengajar)
    await session.commit()

    result = await session.scalars(
        select(GajiPengajar)
        .options(selectinload(GajiPengajar.biodata_user))
        .where(GajiPengajar.id == gaji_pengajar.id)
    )
    return result.one()

@router.patch("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def modify(id: int, payload: GajiPengajarUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    gaji_pengajar = await session.get(GajiPengajar, id)
    if not gaji_pengajar:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(gaji_pengajar, key, val)

    await session.commit()

    result = await session.scalars(
        select(GajiPengajar)
        .options(selectinload(GajiPengajar.biodata_user))
        .where(GajiPengajar.id == gaji_pengajar.id)
    )
    return result.one()

@router.delete("/{id}", response_model=GajiPengajarResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(GajiPengajar)
        .options(selectinload(GajiPengajar.biodata_user))
        .where(GajiPengajar.id == id)
    )
    gaji_pengajar = result.first()
    if not gaji_pengajar:
        raise HTTPException(status_code=404, detail="GajiPengajar tidak ditemukan")

    await session.delete(gaji_pengajar)
    await session.commit()
    return gaji_pengajar

