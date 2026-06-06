from pydantic import BaseModel, ConfigDict
from datetime import date

# Table: Siswa
class SiswaBase(BaseModel):
    alamat: str | None = None

class SiswaCreate(SiswaBase):
    nama: str
    jenis_kelamin: str
    tanggal_lahir: date
    wali_id: int
    kelas_id: int

class SiswaUpdate(SiswaBase):
    nama: str | None = None
    jenis_kelamin: str | None = None
    tanggal_lahir: date | None = None
    wali_id: int | None = None
    kelas_id: int | None = None

class SiswaResponse(SiswaBase):
    id: int
    nama: str
    jenis_kelamin: str
    tanggal_lahir: date
    wali_id: int
    kelas_id: int
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

# Table: Kelas
class KelasBase(BaseModel):
    pass

class KelasCreate(KelasBase):
    nama: str

class KelasUpdate(KelasBase):
    nama: str | None = None

class KelasResponse(KelasBase):
    id: int
    nama: str
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

# Table: Wali
class WaliBase(BaseModel):
    no_hp: str | None = None
    alamat: str | None = None

class WaliCreate(WaliBase):
    nama: str

class WaliUpdate(WaliBase):
    nama: str | None = None

class WaliResponse(WaliBase):
    id: int
    nama: str
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
