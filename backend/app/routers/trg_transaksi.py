from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.sql import or_
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import GajiPengajar, SppSiswa, TrgTransaksi
from app.schemas import TrgTransaksiResponse, TrgTransaksiCreate, TrgTransaksiUpdate
from app.database import get_session
from app.dependencies import allow_bendahara

router = APIRouter(prefix="/trg-transaksi")

dependencies = [Depends(allow_bendahara)]

@router.get("/", response_model=list[TrgTransaksiResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[TrgTransaksi]:
    result = await session.scalars(
        select(TrgTransaksi)
        .options(
            selectinload(TrgTransaksi.spp_siswa)
                .selectinload(SppSiswa.siswa), 
            selectinload(TrgTransaksi.gaji_pengajar)
                .selectinload(GajiPengajar.biodata_user), 
        )
    )
    return list(result.all())

@router.get("/{id}", response_model=TrgTransaksiResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    # trg_transaksi = await session.get(TrgTransaksi, id)
    result = await session.scalars(
        select(TrgTransaksi)
        .options(
            selectinload(TrgTransaksi.spp_siswa)
                .selectinload(SppSiswa.siswa), 
            selectinload(TrgTransaksi.gaji_pengajar)
                .selectinload(GajiPengajar.biodata_user), 
        )
        .where(TrgTransaksi.id == id)
    )
    trg_transaksi = result.first()
    if not trg_transaksi:
        raise HTTPException(status_code=404, detail="TrgTransaksi tidak ditemukan")
    return trg_transaksi

@router.post("/", response_model=TrgTransaksiResponse, dependencies=dependencies)
async def create(payload: TrgTransaksiCreate, session: AsyncSession = Depends(get_session)):
    """Create trg_transaksi"""
    trg_transaksi = TrgTransaksi(**payload.model_dump())
    session.add(trg_transaksi)
    await session.commit()

    result = await session.scalars(
        select(TrgTransaksi)
        .options(
            selectinload(TrgTransaksi.spp_siswa)
                .selectinload(SppSiswa.siswa), 
            selectinload(TrgTransaksi.gaji_pengajar)
                .selectinload(GajiPengajar.biodata_user), 
        )
    )
    trg_transaksi = result.first()
    return trg_transaksi

@router.patch("/{id}", response_model=TrgTransaksiResponse, dependencies=dependencies)
async def modify(id: int, payload: TrgTransaksiUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify trg_transaksi"""
    trg_transaksi = await session.get(TrgTransaksi, id)
    if not trg_transaksi:
        raise HTTPException(status_code=404, detail="TrgTransaksi tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(trg_transaksi, key, val)

    await session.commit()
    # await session.refresh(trg_transaksi)

    result = await session.scalars(
        select(TrgTransaksi)
        .options(
            selectinload(TrgTransaksi.spp_siswa)
                .selectinload(SppSiswa.siswa), 
            selectinload(TrgTransaksi.gaji_pengajar)
                .selectinload(GajiPengajar.biodata_user), 
        )
        .where(TrgTransaksi.id == id)
    )
    return result.first()

@router.delete("/{id}", response_model=TrgTransaksiResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(TrgTransaksi)
        .options(
            selectinload(TrgTransaksi.spp_siswa)
                .selectinload(SppSiswa.siswa), 
            selectinload(TrgTransaksi.gaji_pengajar)
                .selectinload(GajiPengajar.biodata_user), 
        )
        .where(TrgTransaksi.id == id)
    )
    trg_transaksi = result.first()
    # trg_transaksi = await session.get(TrgTransaksi, id)
    if not trg_transaksi:
        raise HTTPException(status_code=404, detail="TrgTransaksi tidak ditemukan")

    await session.delete(trg_transaksi)
    await session.commit()
    return trg_transaksi

