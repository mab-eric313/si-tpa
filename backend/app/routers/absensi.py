from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from datetime import date
from typing import List

from app.models import Absensi
from app.schemas import AbsensiResponse, AbsensiCreate, AbsensiUpdate, AbsensiBulkCreate
from app.database import get_session
from app.dependencies import allow_pengajar

router = APIRouter(prefix="/absensi")

dependencies = [Depends(allow_pengajar)]

@router.get("/tanggal/{target_tanggal}", response_model=List[AbsensiResponse])
async def get_absensi_by_tanggal(
    target_tanggal: date, 
    session: AsyncSession = Depends(get_session)
):
    """Ambil semua data absensi untuk tanggal tertentu"""
    result = await session.scalars(
        select(Absensi)
        .options(selectinload(Absensi.siswa))
        .where(Absensi.tanggal == target_tanggal)
    )
    return list(result.all())

@router.post("/bulk", response_model=List[AbsensiResponse])
async def create_or_update_bulk(
    payload: AbsensiBulkCreate,
    session: AsyncSession = Depends(get_session)
):    
    """Create atau update absensi dalam jumlah banyak (bulk)"""
    results = []
    
    for item in payload.data:
        # Cek apakah sudah ada record untuk siswa + tanggal ini
        existing = await session.scalar(
            select(Absensi).where(
                and_(
                    Absensi.siswa_id == item.siswa_id,
                    Absensi.tanggal == item.tanggal
                )
            )
        )
        
        if existing:
            # Update yang sudah ada
            existing.kehadiran = item.kehadiran
            existing.note = item.note
            results.append(existing)
        else:
            # Buat yang baru
            absensi_baru = Absensi(
                siswa_id=item.siswa_id,
                kehadiran=item.kehadiran,
                tanggal=item.tanggal,
                note=item.note
            )
            session.add(absensi_baru)
            results.append(absensi_baru)
    
    await session.commit()
    
    # Refresh semua results
    for r in results:
        await session.refresh(r)
    
    return results

@router.get("/", response_model=list[AbsensiResponse])
async def get_all(session: AsyncSession = Depends(get_session)) -> list[Absensi]:
    result = await session.scalars(select(Absensi))
    return list(result.all())

@router.get("/{id}", response_model=AbsensiResponse)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    absensi = await session.get(Absensi, id)
    if not absensi:
        raise HTTPException(status_code=404, detail="Absensi tidak ditemukan")
    return absensi

@router.post("/", response_model=AbsensiResponse, dependencies=dependencies)
async def create(payload: AbsensiCreate, session: AsyncSession = Depends(get_session)):
    """Create absensi"""
    absensi = Absensi(**payload.model_dump())
    session.add(absensi)
    await session.commit()
    await session.refresh(absensi)
    return absensi

@router.patch("/{id}", response_model=AbsensiResponse, dependencies=dependencies)
async def modify(id: int, payload: AbsensiUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify absensi"""
    absensi = await session.get(Absensi, id)
    if not absensi:
        raise HTTPException(status_code=404, detail="Absensi tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(absensi, key, val)

    await session.commit()
    await session.refresh(absensi)
    return absensi

@router.delete("/{id}", response_model=AbsensiResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    absensi = await session.get(Absensi, id)
    if not absensi:
        raise HTTPException(status_code=404, detail="Absensi tidak ditemukan")

    await session.delete(absensi)
    await session.commit()
    return absensi


