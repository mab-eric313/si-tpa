import asyncio
import cloudinary.uploader
from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from app.models import PendaftaranSiswa
from app.schemas import (
    PendaftaranSiswaResponse, PendaftaranSiswaCreate, PendaftaranSiswaUpdate,
    PendaftaranSiswaRelatRes
)
from app.database import get_session
from app.dependencies import allow_admin
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/pendaftaran-siswa", tags=["Pendaftaran Siswa"])

dependencies = [Depends(allow_admin)]

async def upload_to_cloudinary(file: UploadFile, folder: str):
    if not file:
        return None
    
    # Baca file
    file_content = await file.read()
    
    # Upload ke Cloudinary (gunakan run_in_threadpool agar async)
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        lambda: cloudinary.uploader.upload(
            file_content,
            folder=folder,
            resource_type="image",
            allowed_formats=["jpg", "png", "jpeg"]
        )
    )
    return result["secure_url"]

@router.get("/", response_model=list[PendaftaranSiswaRelatRes], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[PendaftaranSiswa]:
    result = await session.scalars(
        select(PendaftaranSiswa)
        .options(selectinload(PendaftaranSiswa.kelas))
    )
    if not result:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")
    return list(result.all())

@router.get("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.scalars(
        select(PendaftaranSiswa)
        .options(selectinload(PendaftaranSiswa.kelas))
        .where(PendaftaranSiswa.id == id)
    )
    pendaftaran_siswa = result.first()
    if not pendaftaran_siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")
    return pendaftaran_siswa

@router.post("/", response_model=PendaftaranSiswaResponse)
async def create(payload: PendaftaranSiswaCreate, session: AsyncSession = Depends(get_session)):
    """Create siswa"""
    siswa = PendaftaranSiswa(**payload.model_dump())
    session.add(siswa)
    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.post("/form", response_model=PendaftaranSiswaResponse)
async def create_pendaftaran(
    nama_siswa: str = Form(...),
    status: str = Form(...),
    jenis_kelamin_siswa: str = Form(...),
    tanggal_lahir_siswa: date = Form(...),
    alamat_siswa: str | None = Form(...),
    nama_wali: str = Form(...),
    no_hp_wali: str | None = Form(...),
    alamat_wali: str | None = Form(...),
    kelas_id: int = Form(...),
    foto_kk: UploadFile = File(),
    foto_ak: UploadFile = File(),
    foto_pas: UploadFile = File(),
    session: AsyncSession = Depends(get_session)
):
    url_foto_kk = await upload_to_cloudinary(foto_kk, "si-tpa/kk")
    url_foto_ak = await upload_to_cloudinary(foto_ak, "si-tpa/ak")
    url_foto_pas = await upload_to_cloudinary(foto_pas, "si-tpa/pas")

    pendaftaran_baru = PendaftaranSiswa(
        nama_siswa=nama_siswa,
        status=status,
        jenis_kelamin_siswa=jenis_kelamin_siswa,
        tanggal_lahir_siswa=tanggal_lahir_siswa,
        alamat_siswa=alamat_siswa,
        nama_wali=nama_wali,
        no_hp_wali=no_hp_wali,
        alamat_wali=alamat_wali,
        kelas_id=kelas_id,
        foto_kk=url_foto_kk,
        foto_ak=url_foto_ak,
        foto_pas=url_foto_pas,
    )

    session.add(pendaftaran_baru)
    await session.commit()
    await session.refresh(pendaftaran_baru)

    return pendaftaran_baru

@router.patch("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def modify(id: int, payload: PendaftaranSiswaUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify siswa"""
    siswa = await session.get(PendaftaranSiswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(siswa, key, val)

    await session.commit()
    await session.refresh(siswa)
    return siswa

@router.delete("/{id}", response_model=PendaftaranSiswaResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    siswa = await session.get(PendaftaranSiswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="PendaftaranSiswa tidak ditemukan")

    await session.delete(siswa)
    await session.commit()
    return siswa
