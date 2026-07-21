from app.models import NamaHari, Kehadiran
from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime, time
from typing import List


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None
    role: str | None = None


# Table: Kelas
class KelasBase(BaseModel):
    pass

class KelasCreate(KelasBase):
    nama: str
    start_day: NamaHari
    end_day: NamaHari
    start_time: time
    end_time: time

class KelasUpdate(KelasBase):
    nama: str | None = None
    start_day: NamaHari | None = None
    end_day: NamaHari | None = None
    start_time: time | None = None
    end_time: time | None = None

class KelasResponse(BaseSchema, KelasBase):
    id: int
    nama: str
    start_day: NamaHari
    end_day: NamaHari
    start_time: time
    end_time: time


# Table: PendaftaranSiswa
class PendaftaranSiswaBase(BaseModel):
    alamat_siswa: str | None = None
    no_hp_wali: str | None = None
    alamat_wali: str | None = None

class PendaftaranSiswaCreate(PendaftaranSiswaBase):
    nama_siswa: str
    status: str
    jenis_kelamin_siswa: str
    tanggal_lahir_siswa: date
    nama_wali: str
    kelas_id: int
    foto_kk: str
    foto_ak: str
    foto_pas: str

class PendaftaranSiswaUpdate(PendaftaranSiswaBase):
    nama_siswa: str | None = None
    status: str | None
    jenis_kelamin_siswa: str | None = None
    tanggal_lahir_siswa: date | None = None
    nama_wali: str | None = None
    kelas_id: int | None = None
    foto_kk: str | None = None
    foto_ak: str | None = None
    foto_pas: str | None = None

class PendaftaranSiswaResponse(BaseSchema, PendaftaranSiswaBase):
    id: int
    nama_siswa: str
    status: str
    jenis_kelamin_siswa: str
    tanggal_lahir_siswa: date
    nama_wali: str
    kelas_id: int
    foto_kk: str
    foto_ak: str
    foto_pas: str

class PendaftaranSiswaRelatRes(BaseSchema, PendaftaranSiswaBase):
    id: int
    nama_siswa: str
    status: str
    jenis_kelamin_siswa: str
    tanggal_lahir_siswa: date
    nama_wali: str
    kelas_id: int
    kelas: KelasResponse | None = None
    foto_kk: str
    foto_ak: str
    foto_pas: str


# Table: Siswa
class SiswaBase(BaseModel):
    alamat: str | None = None

class SiswaCreate(SiswaBase):
    nama: str
    jenis_kelamin: str
    tanggal_lahir: date
    wali_id: int
    kelas_id: int

class SiswaRelatCreate(SiswaBase):
    pendaftaran_siswa_id: int
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
    status: str | None = None

class SiswaRelationship(BaseSchema, BaseModel):
    id: int
    nama: str

class SiswaResponse(BaseSchema, SiswaBase):
    id: int
    nama: str
    jenis_kelamin: str
    tanggal_lahir: date
    wali_id: int
    kelas_id: int
    status: str


# Table: Absensi
class AbsensiBase(BaseModel):
    note: str | None = None

class AbsensiCreate(AbsensiBase):
    siswa_id: int
    kehadiran: Kehadiran
    tanggal: date

class AbsensiUpdate(AbsensiBase):
    siswa_id: int | None = None
    kehadiran: Kehadiran | None = None
    tanggal: date | None = None

class AbsensiResponse(BaseSchema, AbsensiBase):
    siswa_id: int
    kehadiran: Kehadiran
    tanggal: date

class AbsensiBulkCreate(BaseModel):
    data: List[AbsensiCreate]


# Table: Wali
class WaliBase(BaseModel):
    no_hp: str | None = None
    alamat: str | None = None

class WaliCreate(WaliBase):
    nama: str

class WaliUpdate(WaliBase):
    nama: str | None = None

class WaliResponse(BaseSchema, WaliBase):
    id: int
    nama: str


# Table: TrgLogSiswa
class TrgLogSiswaBase(BaseModel):
    pass

class TrgLogSiswaCreate(TrgLogSiswaBase):
    siswa_id: int
    kategori_penilaian: str
    lulus_ulang: str
    tanggal: date

class TrgLogSiswaUpdate(BaseModel):
    siswa_id: int | None = None
    kategori_penilaian: str | None = None
    lulus_ulang: str | None = None
    tanggal: date | None = None

class TrgLogSiswaResponse(BaseSchema, TrgLogSiswaBase):
    id: int
    siswa_id: int
    kategori_penilaian: str
    lulus_ulang: str
    tanggal: date


# Table: SppSiswa
class SppSiswaBase(BaseModel):
    tanggal: date | None = None
    pembayaran: int | None = 0
    sisa: int | None = 0

class SppSiswaCreate(SppSiswaBase):
    siswa_id: int
    status: str

class SppSiswaUpdate(BaseModel):
    siswa_id: int | None = None
    tanggal: date | None = None
    pembayaran: int | None = None
    sisa: int | None = None
    status: str | None = None

class SppSiswaResponse(BaseSchema, SppSiswaBase):
    id: int
    siswa_id: int | None
    siswa: SiswaResponse | None = None
    status: str


# Table: BiodataUser
class BiodataUserBase(BaseModel):
    nama_lengkap: str | None = None
    kelas_id: int | None = None
    no_hp: str | None = None
    alamat: str | None = None

class BiodataUserCreate(BiodataUserBase):
    user_id: int
    nama_panggilan: str
    jenis_kelamin: str
    status: str = "Aktif"

class BiodataUserUpdate(BiodataUserBase):
    user_id: int | None = None
    nama_panggilan: str | None = None
    jenis_kelamin: str | None = None
    status: str | None = None

class BiodataUserResponse(BaseSchema, BiodataUserBase):
    id: int
    user_id: int
    nama_panggilan: str
    jenis_kelamin: str
    status: str


# Table: User
class UserBase(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    password: str = Field(
        ..., min_length=8, description="password must be at least 8 characters"
    )
    role: str

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    role: str | None = None

class UserResponse(BaseSchema, UserBase):
    id: int
    role: str
    biodata: BiodataUserResponse | None = None


# Table: GajiPengajar
class GajiPengajarBase(BaseModel):
    gaji: int | None = None

class GajiPengajarCreate(GajiPengajarBase):
    biodata_user_id: int
    tanggal_gaji: date
    status: str

class GajiPengajarUpdate(GajiPengajarBase):
    biodata_user_id: int | None = None
    tanggal_gaji: date | None = None
    status: str | None = None

class GajiPengajarResponse(BaseSchema, GajiPengajarBase):
    id: int
    biodata_user_id: int | None = None
    biodata_user: BiodataUserResponse | None = None
    tanggal_gaji: date
    status: str


# Table: PenggantiPengajar
class PenggantiPengajarBase(BaseModel):
    note: str | None = None

class PenggantiPengajarCreate(PenggantiPengajarBase):
    pengajar_id: int
    pengganti_pengajar_id: int
    kelas_id: int
    tanggal: datetime

class PenggantiPengajarUpdate(PenggantiPengajarBase):
    pengajar_id: int | None = None
    pengganti_pengajar_id: int | None = None
    kelas_id: int | None = None
    tanggal: datetime | None = None

class PenggantiPengajarResponse(BaseSchema, PenggantiPengajarBase):
    id: int
    pengajar_id: int
    pengganti_pengajar_id: int
    kelas_id: int
    tanggal: datetime


# Table: TrgTransaksi
class TrgTransaksiBase(BaseModel):
    note: str | None = None
    spp_siswa_id: int | None = None
    gaji_pengajar_id: int | None = None

class TrgTransaksiCreate(TrgTransaksiBase):
    kategori: str
    tanggal: date
    nama: str
    nominal: int

class TrgTransaksiUpdate(TrgTransaksiBase):
    kategori: str | None = None
    tanggal: date | None = None
    nama: str | None = None
    nominal: int | None = None

class TrgTransaksiResponse(BaseSchema, TrgTransaksiBase):
    id: int
    kategori: str
    tanggal: date
    nama: str
    nominal: int
    gaji_pengajar: GajiPengajarResponse | None = None
    spp_siswa: SppSiswaResponse | None = None


# Table: PenilaianSurat
class PenilaianSuratBase(BaseModel):
    lulus_ulang: str | None = None
    note: str | None = None

class PenilaianSuratCreate(PenilaianSuratBase):
    siswa_id: int
    nama_surat: str
    tanggal_setor: date
    kelancaran: int
    ketepatan_bacaan: int
    # waktu_penilaian: str = "Harian"

class PenilaianSuratUpdate(PenilaianSuratBase):
    siswa_id: int | None = None
    nama_surat: str | None = None
    tanggal_setor: date | None = None
    kelancaran: int | None = None
    ketepatan_bacaan: int | None = None
    # waktu_penilaian: str | None = None

class PenilaianSuratResponse(BaseSchema, PenilaianSuratBase):
    id: int
    siswa_id: int
    siswa: SiswaRelationship
    nama_surat: str
    tanggal_setor: date
    kelancaran: int
    ketepatan_bacaan: int
    # waktu_penilaian: str
    updated_at: datetime


# Table: PenilaianDoa
class PenilaianDoaBase(BaseModel):
    lulus_ulang: str | None = None
    note: str | None = None

class PenilaianDoaCreate(PenilaianDoaBase):
    siswa_id: int
    nama_doa: str
    tanggal_setor: date
    nilai: int
    # waktu_penilaian: str = "Harian"

class PenilaianDoaUpdate(PenilaianDoaBase):
    siswa_id: int | None = None
    nama_doa: str | None = None
    tanggal_setor: date | None = None
    nilai: int | None = None
    # waktu_penilaian: str | None = None

class PenilaianDoaResponse(BaseSchema, PenilaianDoaBase):
    id: int
    siswa_id: int
    siswa: SiswaRelationship
    nama_doa: str
    tanggal_setor: date
    nilai: int
    # waktu_penilaian: str
    updated_at: datetime


# Table: PenilaianJilid
class PenilaianJilidBase(BaseModel):
    lulus_ulang: str | None = None
    note: str | None = None

class PenilaianJilidCreate(PenilaianJilidBase):
    siswa_id: int
    materi_bacaan: str
    tanggal_setor: date
    nilai_tajwid: int
    nilai_makhraj: int
    nilai_kelancaran: int
    # waktu_penilaian: str = "Harian"

class PenilaianJilidUpdate(PenilaianJilidBase):
    siswa_id: int | None = None
    materi_bacaan: str | None = None
    tanggal_setor: date | None = None
    nilai_tajwid: int | None = None
    nilai_makhraj: int | None = None
    nilai_kelancaran: int | None = None
    # waktu_penilaian: str | None = None

class PenilaianJilidResponse(BaseSchema, PenilaianJilidBase):
    id: int
    siswa_id: int
    siswa: SiswaRelationship
    materi_bacaan: str
    tanggal_setor: date
    nilai_tajwid: int
    nilai_makhraj: int
    nilai_kelancaran: int
    # waktu_penilaian: str
    updated_at: datetime


# Relationship
class SiswaRelatRes(BaseSchema, SiswaBase):
    id: int
    nama: str
    jenis_kelamin: str
    tanggal_lahir: date
    wali_id: int
    wali: WaliResponse | None = None
    kelas_id: int
    kelas: KelasResponse | None = None
    pendaftaran_siswa_id: int | None = None
    pendaftaran_siswa: PendaftaranSiswaResponse | None = None
    status: str

