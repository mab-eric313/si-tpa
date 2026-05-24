# TODO: (LOW) Is models module needed? Currently this module is not used.
# Use this when real data is ready
# or maybe this file is not required

# from typing import Annotated
# from sqlmodel import Session, SQLModel, create_engine
# from fastapi import Depends
# from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
# 
# DB_URL = (f"mariadb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
# connect_args = {"check_same_thread": False}
# engine = create_engine(DB_URL, connect_args=connect_args)
# 
# def create_db():
#     SQLModel.metadata.create_all(engine)
# 
# def get_session():
#     with Session(engine) as session:
#         yield session
# 
# SessionDep = Annotated[Session, Depends(get_session)]

from sqlalchemy import JSON, Date, Enum, Integer, Column, String
from pydantic import BaseModel, ConfigDict, Field
import datetime as dt
from datetime import date
from .init import Base

class SiswaBaseResponse(BaseModel):
    id: int | None = None
    nama: str | None = None
    jenis_kelamin: str | None = None
    tanggal_lahir: date | None = None
    alamat: str | None = None
    wali_id: int | None = None
    kelas_id: int | None = None
    metadata: dict[str, str] | None = Field(default=None, alias="metadata_")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class Siswa(Base):
    __tablename__ = "siswa"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(String(45), nullable=False)
    jenis_kelamin = Column(Enum("L", "P"), nullable=False)
    tanggal_lahir = Column(Date(), nullable=False)
    alamat = Column(String(45), nullable=False)
    wali_id = Column(Integer, nullable=False)
    kelas_id = Column(Integer, nullable=False)

    metadata_ = Column("metadata", JSON)

siswa = Siswa(
    id=1, nama="Budi", jenis_kelamin="L", tanggal_lahir=None, 
    alamat="Indonesia", wali_id=11, kelas_id=111
)
pydantic_siswa = SiswaBaseResponse.model_validate(siswa)

# sql_model = Siswa(metadata_={"key": "val"}, id=1)
# pydantic_model = SiswaBase.model_validate(sql_model)

# print(pydantic_model.model_dump())
#> {'metadata': {'key': 'val'}}
# print(pydantic_model.model_dump(by_alias=True))
#> {'metadata_': {'key': 'val'}}
