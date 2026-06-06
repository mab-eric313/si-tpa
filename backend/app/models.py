from sqlalchemy import Date, Enum, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

# NOTE: Type data conventions
# nama: String(150)
# alamat: String(255)
# no_hp: String(20)

class Siswa(Base):
    __tablename__ = "siswa"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    jenis_kelamin: Mapped[str] = mapped_column(Enum("L", "P"), nullable=False)
    tanggal_lahir: Mapped[Date] = mapped_column(Date(), nullable=False)
    alamat: Mapped[str | None] = mapped_column(String(255), nullable=True)

    wali_id: Mapped[int] = mapped_column(Integer, ForeignKey("wali.id"), nullable=False)
    kelas_id: Mapped[int] = mapped_column(Integer, ForeignKey("kelas.id"), nullable=False)

class Kelas(Base):
    __tablename__ = "kelas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nama: Mapped[str] = mapped_column(
        Enum("jilid_1-3", "jilid_4-6", "alquran"), nullable=False
    )

class Wali(Base):
    __tablename__ = "wali"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    no_hp: Mapped[str | None] = mapped_column(String(20), nullable=True)
    alamat: Mapped[str | None] = mapped_column(String(255), nullable=True)
