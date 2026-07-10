from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    Siswa, PendaftaranSiswa, PendaftaranSiswaStatus, StatusSiswa, Wali
)
from app.schemas import (
    SiswaResponse, SiswaCreate, SiswaUpdate, SiswaRelatRes
)
from app.database import get_session
from app.dependencies import allow_pengajar, allow_all
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/siswa")

read_dependencies = [Depends(allow_all)]
write_dependencies = [Depends(allow_pengajar)]

@router.get("/", response_model=list[SiswaRelatRes], dependencies=read_dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[Siswa]:
    result = await session.scalars(
        select(Siswa)
        .options(
            selectinload(Siswa.pendaftaran_siswa)
            .selectinload(PendaftaranSiswa.kelas)
        ).options(
            selectinload(Siswa.wali)
        ).options(
            selectinload(Siswa.kelas)
        )
    )
    return list(result.all())

@router.get("/", response_model=list[SiswaRelatRes], dependencies=read_dependencies)
async def get_all_active(session: AsyncSession = Depends(get_session)) -> list[Siswa]:
    result = await session.scalars(
        select(Siswa)
        .options(
            selectinload(Siswa.pendaftaran_siswa)
            .selectinload(PendaftaranSiswa.kelas)
        ).options(
            selectinload(Siswa.wali)
        ).options(
            selectinload(Siswa.kelas)
        ).where(Siswa.status == StatusSiswa.AKTIF)
    )
    return list(result.all())

@router.get("/{id}", response_model=SiswaRelatRes, dependencies=read_dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(Siswa)
        .options(
            selectinload(Siswa.pendaftaran_siswa)
            .selectinload(PendaftaranSiswa.kelas)
        ).options(
            selectinload(Siswa.wali)
        ).options(
            selectinload(Siswa.kelas)
        ).where(Siswa.id == id)
    )
    siswa = result.first()
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    return siswa

@router.post("/", response_model=SiswaResponse, dependencies=write_dependencies)
async def create(payload: SiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create siswa"""
    siswa = Siswa(**payload.model_dump())
    session.add(siswa)
    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.post("/{id}", response_model=SiswaRelatRes, dependencies=write_dependencies)
async def create_from_pendaftaran_siswa(
    id: int, session: AsyncSession = Depends(get_session)
):
    """Create siswa from pendaftaran_siswa"""
    pendaftaran_siswa = await session.get(PendaftaranSiswa, id)
    if not pendaftaran_siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")

    wali = Wali(nama=pendaftaran_siswa.nama_wali, alamat=pendaftaran_siswa.alamat_wali, no_hp=pendaftaran_siswa.no_hp_wali)
    session.add(wali)
    await session.flush()
    wali_id = wali.id

    siswa = Siswa(
        nama=pendaftaran_siswa.nama_siswa,
        jenis_kelamin=pendaftaran_siswa.jenis_kelamin_siswa,
        tanggal_lahir=pendaftaran_siswa.tanggal_lahir_siswa,
        kelas_id=pendaftaran_siswa.kelas_id,
        alamat=pendaftaran_siswa.alamat_siswa,
        pendaftaran_siswa_id=pendaftaran_siswa.id,
        wali_id=wali_id
    )
    
    session.add(siswa)

    pendaftaran_siswa.status = PendaftaranSiswaStatus.DITERIMA
    await session.commit()

    result = await session.scalars(
        select(Siswa)
        .options(
            selectinload(Siswa.pendaftaran_siswa)
            .selectinload(PendaftaranSiswa.kelas)
        ).options(
            selectinload(Siswa.wali)
        ).options(
            selectinload(Siswa.kelas)
        ).where(Siswa.id == siswa.id)
    )
    return result.one()

@router.patch("/{id}", response_model=SiswaResponse, dependencies=write_dependencies)
async def modify(id: int, payload: SiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify siswa"""
    siswa = await session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(siswa, key, val)

    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.delete("/{id}", response_model=SiswaResponse, dependencies=write_dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    siswa = await session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    await session.delete(siswa)
    await session.commit()
    return siswa
