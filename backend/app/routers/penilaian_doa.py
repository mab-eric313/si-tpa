from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PenilaianDoa
from app.schemas import PenilaianDoaResponse, PenilaianDoaCreate, PenilaianDoaUpdate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/penilaian-doa")

dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[PenilaianDoaResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PenilaianDoa]:
    result = await session.scalars(
        select(PenilaianDoa)
        .options(selectinload(PenilaianDoa.siswa))
    )
    return list(result.all())

@router.get("/{id}", response_model=PenilaianDoaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianDoa)
        .options(selectinload(PenilaianDoa.siswa))
        .where(PenilaianDoa.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianDoa tidak ditemukan")
    return penilaian

@router.post("/", response_model=PenilaianDoaResponse, dependencies=dependencies)
async def create(payload: PenilaianDoaCreate, session: AsyncSession = Depends(get_session)):
    """Create penilaian"""
    penilaian = PenilaianDoa(**payload.model_dump())
    session.add(penilaian)
    await session.commit()

    result = await session.scalars(
        select(PenilaianDoa)
        .options(selectinload(PenilaianDoa.siswa))
        .where(PenilaianDoa.id == penilaian.id)
    )
    return result.one()

@router.patch("/{id}", response_model=PenilaianDoaResponse, dependencies=dependencies)
async def modify(id: int, payload: PenilaianDoaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify penilaian"""
    penilaian = await session.get(PenilaianDoa, id)
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianDoa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(penilaian, key, val)

    await session.commit()

    result = await session.scalars(
        select(PenilaianDoa)
        .options(selectinload(PenilaianDoa.siswa))
        .where(PenilaianDoa.id == penilaian.id)
    )
    return result.one()

@router.delete("/{id}", response_model=PenilaianDoaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PenilaianDoa)
        .options(selectinload(PenilaianDoa.siswa))
        .where(PenilaianDoa.id == id)
    )
    penilaian = result.first()
    if not penilaian:
        raise HTTPException(status_code=404, detail="PenilaianDoa tidak ditemukan")

    await session.delete(penilaian)
    await session.commit()
    return penilaian
