from sqlalchemy import Date, Enum, ForeignKey, Integer, Column, String
from app.database import Base

# TODO: (HIGH) Replace Column() with Mapped[] and mapped_column()
class Siswa(Base):
    __tablename__ = "siswa"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(String(45), nullable=False)
    jenis_kelamin = Column(Enum("L", "P"), nullable=False)
    tanggal_lahir = Column(Date(), nullable=False)
    alamat = Column(String(45), nullable=True)

    wali_id = Column(Integer, ForeignKey("wali.id"), nullable=False)
    kelas_id = Column(Integer, ForeignKey("kelas.id"), nullable=False)

class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(Enum("jilid_1-3", "jilid_4-6", "alquran"), nullable=False)

class Wali(Base):
    __tablename__ = "wali"

    id = Column(Integer, primary_key=True, nullable=False)
    nama = Column(String(45), nullable=False)
    no_hp = Column(String(45), nullable=True)
    alamat = Column(String(45), nullable=True)

