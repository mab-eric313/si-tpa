from sqlalchemy import Date, Enum, Integer, Column, String
from app.database import Base

class Siswa(Base):
    __tablename__ = "siswa"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(String(45), nullable=False)
    jenis_kelamin = Column(Enum("L", "P"), nullable=False)
    tanggal_lahir = Column(Date(), nullable=False)
    alamat = Column(String(45), nullable=False)
    wali_id = Column(Integer, nullable=False)
    kelas_id = Column(Integer, nullable=False)
