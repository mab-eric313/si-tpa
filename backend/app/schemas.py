from pydantic import BaseModel, ConfigDict
from datetime import date

class SiswaBase(BaseModel):
    id: int | None = None
    nama: str | None = None
    jenis_kelamin: str | None = None
    tanggal_lahir: date | None = None
    alamat: str | None = None
    wali_id: int | None = None
    kelas_id: int | None = None

class SiswaResponse(SiswaBase):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class SiswaCreate(SiswaBase):
    pass

class SiswaUpdate(BaseModel):
    nama: str | None = None
    jenis_kelamin: str | None = None
    tanggal_lahir: date | None = None
    alamat: str | None = None
    wali_id: int | None = None
    kelas_id: int | None = None
