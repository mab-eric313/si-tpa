from datetime import date, datetime
from enum import Enum as PyEnum
from typing import Optional, List
from sqlalchemy import (
    ForeignKey, String, Integer, Date, DateTime, TIMESTAMP,Enum, text, event, 
    inspect, Time
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
)

# NOTE: Type data conventions
# nama: String(150)
# alamat: String(255)
# no_hp: String(20)


class Base(DeclarativeBase):
    pass


# Enums
class JenisKelamin(str, PyEnum):
    L = "L"
    P = "P"

class KategoriPenilaian(str, PyEnum):
    HAFALAN_SURAT = "Hafalan Surat"
    HAFALAN_DOA = "Hafalan Doa"
    BACAAN_JILID = "Bacaan Jilid"

class LulusUlang(str, PyEnum):
    LULUS = "Lulus"
    ULANG = "Ulang"

class StatusSpp(str, PyEnum):
    LUNAS = "Lunas"
    BELUM_LUNAS = "Belum Lunas"

class UserRole(str, PyEnum):
    PENGAJAR = "Pengajar"
    BENDAHARA = "Bendahara"
    ADMIN = "Admin"

class StatusUser(str, PyEnum):
    AKTIF = "Aktif"
    TIDAK_AKTIF = "Tidak Aktif"

class StatusGaji(str, PyEnum):
    SUDAH_DIGAJI = "Sudah digaji"
    BELUM_DIGAJI = "Belum digaji"

class KategoriTransaksi(str, PyEnum):
    PEMASUKAN = "Pemasukan"
    PENGELUARAN = "Pengeluaran"

class WaktuPenilaian(str, PyEnum):
    HARIAN = "Harian"
    BULANAN = "Bulanan"

class PendaftaranSiswaStatus(str, PyEnum):
    DITERIMA = "Diterima"
    PENDING = "Pending"
    DITOLAK = "Ditolak"

class StatusSiswa(str, PyEnum):
    AKTIF = "Aktif"
    TIDAK_AKTIF = "Tidak Aktif"

class NamaHari(str, PyEnum):
    SENIN = "Senin"
    SELASA = "Selasa"
    RABU = "Rabu"
    KAMIS = "Kamis"
    JUMAT = "Jumat"
    SABTU = "Sabtu"
    MINGGU = "Minggu"


# Tables
class Wali(Base):
    __tablename__ = "wali"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    no_hp: Mapped[Optional[str]] = mapped_column(String(20))
    alamat: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    siswas: Mapped[List["Siswa"]] = relationship(back_populates="wali")


class Kelas(Base):
    __tablename__ = "kelas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    start_day: Mapped[NamaHari] = mapped_column(Enum(NamaHari), nullable=False)
    end_day: Mapped[NamaHari] = mapped_column(Enum(NamaHari), nullable=False)
    start_time: Mapped[Time] = mapped_column(Time, nullable=False)
    end_time: Mapped[Time] = mapped_column(Time, nullable=False)

    # Relationships
    pendaftaran_siswa: Mapped[List["PendaftaranSiswa"]] = relationship(back_populates="kelas")
    siswas: Mapped[List["Siswa"]] = relationship(back_populates="kelas")
    biodata_users: Mapped[List["BiodataUser"]] = relationship(back_populates="kelas")
    pengganti_transaksi: Mapped[List["PenggantiPengajar"]] = relationship(back_populates="kelas")


class PendaftaranSiswa(Base):
    __tablename__ = "pendaftaran_siswa"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nama_siswa: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[str] = mapped_column(Enum(PendaftaranSiswaStatus), nullable=False)
    jenis_kelamin_siswa: Mapped[JenisKelamin] = mapped_column(Enum(JenisKelamin), nullable=False)
    tanggal_lahir_siswa: Mapped[date] = mapped_column(Date, nullable=False)
    alamat_siswa: Mapped[Optional[str]] = mapped_column(String(255))
    nama_wali: Mapped[str] = mapped_column(String(150), nullable=False)
    no_hp_wali: Mapped[Optional[str]] = mapped_column(String(20))
    alamat_wali: Mapped[Optional[str]] = mapped_column(String(255))
    kelas_id: Mapped[int] = mapped_column(ForeignKey("kelas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    # siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)

    # Relationships
    kelas: Mapped["Kelas"] = relationship(back_populates="pendaftaran_siswa")
    siswa: Mapped["Siswa"] = relationship(back_populates="pendaftaran_siswa", uselist=False)


class Siswa(Base):
    __tablename__ = "siswa"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    jenis_kelamin: Mapped[JenisKelamin] = mapped_column(Enum(JenisKelamin), nullable=False)
    tanggal_lahir: Mapped[date] = mapped_column(Date, nullable=False)
    alamat: Mapped[Optional[str]] = mapped_column(String(255))
    wali_id: Mapped[int] = mapped_column(ForeignKey("wali.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    kelas_id: Mapped[int] = mapped_column(ForeignKey("kelas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    pendaftaran_siswa_id: Mapped[int] = mapped_column(ForeignKey("pendaftaran_siswa.id"), unique=True, nullable=True)
    status: Mapped[str] = mapped_column(Enum(StatusSiswa), nullable=False, default=StatusSiswa.AKTIF)

    # Relationships
    wali: Mapped["Wali"] = relationship(back_populates="siswas")
    kelas: Mapped["Kelas"] = relationship(back_populates="siswas")
    logs: Mapped[List["TrgLogSiswa"]] = relationship(back_populates="siswa")
    spp_records: Mapped[List["SppSiswa"]] = relationship(back_populates="siswa")
    pendaftaran_siswa: Mapped["PendaftaranSiswa"] = relationship(back_populates="siswa")


class TrgLogSiswa(Base):
    __tablename__ = "trg_log_siswa"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    kategori_penilaian: Mapped[KategoriPenilaian] = mapped_column(Enum(KategoriPenilaian), nullable=False)
    lulus_ulang: Mapped[LulusUlang] = mapped_column(Enum(LulusUlang), nullable=False)
    tanggal: Mapped[date] = mapped_column(Date, nullable=False)

    # Relationships
    siswa: Mapped["Siswa"] = relationship(back_populates="logs")


class SppSiswa(Base):
    __tablename__ = "spp_siswa"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    tanggal: Mapped[Optional[date]] = mapped_column(Date)
    pembayaran: Mapped[Optional[int]] = mapped_column(Integer, default=0)
    sisa: Mapped[Optional[int]] = mapped_column(Integer, default=0)
    status: Mapped[StatusSpp] = mapped_column(Enum(StatusSpp), nullable=False, default=StatusSpp.BELUM_LUNAS)

    # Relationships
    siswa: Mapped["Siswa"] = relationship(back_populates="spp_records")
    transaksis: Mapped[List["TrgTransaksi"]] = relationship(back_populates="spp_siswa")


class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(45), nullable=False)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, 
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        nullable=False
    )

    # Relationships
    biodata: Mapped[Optional["BiodataUser"]] = relationship(back_populates="user")


class BiodataUser(Base):
    __tablename__ = "biodata_user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"), unique=True, nullable=False)
    nama_lengkap: Mapped[Optional[str]] = mapped_column(String(150))
    nama_panggilan: Mapped[str] = mapped_column(String(150), nullable=False)
    jenis_kelamin: Mapped[JenisKelamin] = mapped_column(Enum(JenisKelamin), nullable=False)
    status: Mapped[StatusUser] = mapped_column(Enum(StatusUser), nullable=False, default=StatusUser.AKTIF)
    kelas_id: Mapped[Optional[int]] = mapped_column(ForeignKey("kelas.id", ondelete="SET NULL", onupdate="CASCADE"))
    no_hp: Mapped[Optional[str]] = mapped_column(String(20))
    alamat: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="biodata")
    kelas: Mapped[Optional["Kelas"]] = relationship(back_populates="biodata_users")
    gaji_records: Mapped[List["GajiPengajar"]] = relationship(back_populates="biodata_user")


class GajiPengajar(Base):
    __tablename__ = "gaji_pengajar"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    biodata_user_id: Mapped[int] = mapped_column(ForeignKey("biodata_user.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    gaji: Mapped[Optional[int]] = mapped_column(Integer)
    tanggal_gaji: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[StatusGaji] = mapped_column(Enum(StatusGaji), nullable=False, default=StatusGaji.BELUM_DIGAJI)

    # Relationships
    biodata_user: Mapped["BiodataUser"] = relationship(back_populates="gaji_records")
    transaksis: Mapped[List["TrgTransaksi"]] = relationship(back_populates="gaji_pengajar")


class PenggantiPengajar(Base):
    __tablename__ = "pengganti_pengajar"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pengajar_id: Mapped[int] = mapped_column(ForeignKey("biodata_user.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    pengganti_pengajar_id: Mapped[int] = mapped_column(ForeignKey("biodata_user.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    kelas_id: Mapped[int] = mapped_column(ForeignKey("kelas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    tanggal: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    note: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    kelas: Mapped["Kelas"] = relationship(back_populates="pengganti_transaksi")
    pengajar: Mapped["BiodataUser"] = relationship("BiodataUser", foreign_keys=[pengajar_id])
    pengganti: Mapped["BiodataUser"] = relationship("BiodataUser", foreign_keys=[pengganti_pengajar_id])


class TrgTransaksi(Base):
    __tablename__ = "trg_transaksi"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kategori: Mapped[KategoriTransaksi] = mapped_column(Enum(KategoriTransaksi), nullable=False)
    tanggal: Mapped[date] = mapped_column(Date, nullable=False)
    nama: Mapped[str] = mapped_column(String(150), nullable=False)
    note: Mapped[Optional[str]] = mapped_column(String(255))
    nominal: Mapped[int] = mapped_column(Integer, nullable=False)
    spp_siswa_id: Mapped[Optional[int]] = mapped_column(ForeignKey("spp_siswa.id", ondelete="CASCADE", onupdate="CASCADE"))
    gaji_pengajar_id: Mapped[Optional[int]] = mapped_column(ForeignKey("gaji_pengajar.id", ondelete="CASCADE", onupdate="CASCADE"))

    # Relationships
    spp_siswa: Mapped[Optional["SppSiswa"]] = relationship(back_populates="transaksis")
    gaji_pengajar: Mapped[Optional["GajiPengajar"]] = relationship(back_populates="transaksis")

    # Constraint XOR
    # __table_args__ = (
    #     CheckConstraint(
    #         # Opsi 1:
    #         # "(`spp_siswa_id` IS NOT NULL AND `gaji_pengajar_id` IS NULL) OR (`spp_siswa_id` IS NULL AND `gaji_pengajar_id` IS NOT NULL)",
    #         name="chk_transaksi_exclusivity"
    #     ),
    # )


class BasePenilaian:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tanggal_setor: Mapped[date] = mapped_column(Date, nullable=False)
    lulus_ulang: Mapped[Optional[LulusUlang]] = mapped_column(Enum(LulusUlang))
    note: Mapped[Optional[str]] = mapped_column(String(255))
    # waktu_penilaian: Mapped[WaktuPenilaian] = mapped_column(Enum(WaktuPenilaian), nullable=False, default=WaktuPenilaian.HARIAN)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        nullable=False
    )

    # Relationship
    @declared_attr
    def siswa(cls) -> Mapped["Siswa"]:
        return relationship("Siswa")


class PenilaianSurat(Base, BasePenilaian):
    __tablename__ = "penilaian_surat"
    siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    nama_surat: Mapped[str] = mapped_column(String(45), nullable=False)
    kelancaran: Mapped[int] = mapped_column(Integer, nullable=False)
    ketepatan_bacaan: Mapped[int] = mapped_column(Integer, nullable=False)

class PenilaianDoa(Base, BasePenilaian):
    __tablename__ = "penilaian_doa"
    siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    nama_doa: Mapped[str] = mapped_column(String(45), nullable=False)
    nilai: Mapped[int] = mapped_column(Integer, nullable=False)

class PenilaianJilid(Base, BasePenilaian):
    __tablename__ = "penilaian_jilid"
    siswa_id: Mapped[int] = mapped_column(ForeignKey("siswa.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    materi_bacaan: Mapped[str] = mapped_column(String(45), nullable=False)
    nilai_tajwid: Mapped[int] = mapped_column(Integer, nullable=False)
    nilai_makhraj: Mapped[int] = mapped_column(Integer, nullable=False)
    nilai_kelancaran: Mapped[int] = mapped_column(Integer, nullable=False)
    nilai_akhir: Mapped[int] = mapped_column(Integer, nullable=False)


# Triggers
@event.listens_for(TrgTransaksi, "before_insert")
@event.listens_for(TrgTransaksi, "before_update")
def validate_transaksi_exclusivity(mapper, connection, target: TrgTransaksi):
    state = inspect(target)

    spp_id = state.dict.get('spp_siswa_id', target.spp_siswa_id)
    gaji_id = state.dict.get('gaji_pengajar_id', target.gaji_pengajar_id)

    print(f"DEBUG -> nama={target.nama}, spp_id={spp_id!r}, gaji_id={gaji_id!r}")

    is_spp_set = spp_id is not None
    is_gaji_set = gaji_id is not None

    if is_spp_set == is_gaji_set:
        raise ValueError(
            "Kolom 'spp_siswa_id' dan 'gaji_pengajar_id' harus salah satu diisi "
            "(tidak boleh keduanya kosong maupun keduanya terisi)."
        )

@event.listens_for(PenilaianSurat, "after_insert")
def log_surat_after_insert(mapper, connection, target):
    connection.execute(
        text("""
             INSERT INTO trg_log_siswa (
                 siswa_id, 
                 kategori_penilaian, 
                 lulus_ulang, 
                 tanggal
             ) VALUES (:siswa_id, :kategori, :status, :tgl)
        """),
        {
            "siswa_id": target.siswa_id, 
            "kategori": "HAFALAN_SURAT", 
            "status": target.lulus_ulang, 
            "tgl": target.tanggal_setor
        }
    )

@event.listens_for(PenilaianDoa, "after_insert")
def log_doa_after_insert(mapper, connection, target):
    connection.execute(
        text("""
            INSERT INTO trg_log_siswa (
                 siswa_id, 
                 kategori_penilaian, 
                 lulus_ulang, tanggal
             ) VALUES (:siswa_id, :kategori, :status, :tgl)
         """),
        {
            "siswa_id": target.siswa_id, 
            "kategori": "HAFALAN_DOA", 
            "status": target.lulus_ulang, 
            "tgl": target.tanggal_setor
        }
    )

@event.listens_for(PenilaianJilid, "after_insert")
def log_jilid_after_insert(mapper, connection, target):
    connection.execute(
        text("""
            INSERT INTO trg_log_siswa (
                siswa_id, 
                kategori_penilaian, 
                lulus_ulang, tanggal
            ) VALUES (:siswa_id, :kategori, :status, :tgl)
        """),
        {
            "siswa_id": target.siswa_id, 
            "kategori": "BACAAN_JILID", 
            "status": target.lulus_ulang, 
            "tgl": target.tanggal_setor
        }
    )

@event.listens_for(TrgTransaksi, "after_insert")
def transaksi_after_insert(mapper, connection, target):
    if target.spp_siswa_id is not None:
        connection.execute(
            text("""
                UPDATE spp_siswa 
                SET tanggal = :tgl,
                    pembayaran = COALESCE(pembayaran, 0) + :nominal,
                    sisa = GREATEST(0, COALESCE(sisa, 0) - :nominal),
                    status = CASE WHEN GREATEST(0, COALESCE(sisa, 0) - :nominal) = 0 THEN 'Lunas' ELSE 'Belum Lunas' END
                WHERE id = :spp_id
            """),
            {
                "tgl": target.tanggal, 
                "nominal": target.nominal, 
                "spp_id": target.spp_siswa_id
            }
        )
    
    if target.gaji_pengajar_id is not None:
        connection.execute(
            text("""
                UPDATE gaji_pengajar 
                SET status = 'SUDAH_DIGAJI',
                    tanggal_gaji = :tgl,
                    gaji = :nominal
                WHERE id = :gaji_id
            """),
            {
                "tgl": target.tanggal, 
                "nominal": target.nominal, 
                "gaji_id": target.gaji_pengajar_id
            }
        )
