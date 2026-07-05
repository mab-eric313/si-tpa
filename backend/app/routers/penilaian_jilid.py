from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PenilaianJilid
from app.schemas import PenilaianJilidResponse, PenilaianJilidCreate, PenilaianJilidUpdate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/penilaian-jilid")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[PenilaianJilidResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PenilaianJilid]:
    result = await session.scalars(
        select(PenilaianJilid)
        .options(selectinload(PenilaianJilid.siswa))
    )
    return list(result.all())

@router.get("/{id}", response_model=PenilaianJilidResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianJilid)
        .options(selectinload(PenilaianJilid.siswa))
        .where(PenilaianJilid.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianJilid tidak ditemukan")
    return penilaian

@router.post("/", response_model=PenilaianJilidResponse, dependencies=dependencies)
async def create(payload: PenilaianJilidCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    penilaian = PenilaianJilid(**payload.model_dump())
    session.add(penilaian)
    await session.commit()

    result = await session.scalars(
        select(PenilaianJilid)
        .options(selectinload(PenilaianJilid.siswa))
        .where(PenilaianJilid.id == penilaian.id)
    )
    return result.one()

@router.patch("/{id}", response_model=PenilaianJilidResponse, dependencies=dependencies)
async def modify(id: int, payload: PenilaianJilidUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify penilaian"""
    penilaian = await session.get(PenilaianJilid, id)
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianJilid tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(penilaian, key, val)

    await session.commit()
    result = await session.scalars(
        select(PenilaianJilid)
        .options(selectinload(PenilaianJilid.siswa))
        .where(PenilaianJilid.id == penilaian.id)
    )
    return result.one()

@router.delete("/{id}", response_model=PenilaianJilidResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianJilid)
        .options(selectinload(PenilaianJilid.siswa))
        .where(PenilaianJilid.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianJilid tidak ditemukan")

    await session.delete(penilaian)
    await session.commit()
    return penilaian

