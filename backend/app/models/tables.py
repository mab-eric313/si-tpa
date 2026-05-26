from sqlalchemy import Date, Enum, Integer, Column, String
from pydantic import BaseModel, ConfigDict
from datetime import date
from .init import Base
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

class Siswa(Base):
    __tablename__ = "siswa"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(String(45), nullable=False)
    jenis_kelamin = Column(Enum("L", "P"), nullable=False)
    tanggal_lahir = Column(Date(), nullable=False)
    alamat = Column(String(45), nullable=False)
    wali_id = Column(Integer, nullable=False)
    kelas_id = Column(Integer, nullable=False)
