"""
Take note this file is for development only

The purpose of this file is to create users and populate records, 
so you can login using this pre-configured username and password.

# Pengajar
    - username: pengajar1
    - password: pengajar1234

    - username: pengajar2
    - password: pengajar1234

# Bendahara
    - username: bendahara1
    - password: bendahara1234

    - username: bendahara2
    - password: bendahara1234

# Admin
    - username: admin
    - password: admin1234
"""

import requests
import sys

BASE_URL = "http://localhost:8000"

admin = [
    {"username": "admin1", "password": "admin1234", "role": "Admin"},
]

pengajar = [
    {"username": "pengajar1", "password": "pengajar1234", "role": "Pengajar"},
    {"username": "pengajar2", "password": "pengajar1234", "role": "Pengajar"},
    {"username": "pengajar3", "password": "pengajar1234", "role": "Pengajar"},
    {"username": "pengajar4", "password": "pengajar1234", "role": "Pengajar"},
    {"username": "pengajar5", "password": "pengajar1234", "role": "Pengajar"}
]

bendahara = [
    {"username": "bendahara1", "password": "bendahara1234", "role": "Bendahara"},
    {"username": "bendahara2", "password": "bendahara1234", "role": "Bendahara"}
]

kelas = [
    {"nama": "Jilid 1-3", "start_day": "Senin", "end_day": "Sabtu", "start_time": "13:00", "end_time": "14:30"},
    {"nama": "Jilid 4-6", "start_day": "Senin", "end_day": "Sabtu", "start_time": "15:30", "end_time": "17:00"},
    {"nama": "Al-Quran", "start_day": "Senin", "end_day": "Sabtu", "start_time": "18:00", "end_time": "18:30"},
]

wali = [
    {"nama": "Budi Wibowo", "no_hp": "081234567890", "alamat": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik"},
    {"nama": "Zulfikar Hasan", "no_hp": "081234567891", "alamat": ""},
    {"nama": "Sutrisno Hadi", "no_hp": "081234567892", "alamat": "Jl. Sunan Giri, Desa Giri, Kec. Kebomas"},
    {"nama": "Siti Aminah", "no_hp": "081234567893", "alamat": "Jl. Dr. Sutomo, Kel. Tlogopatut, Kec. Gresik"},
    {"nama": "Rahman Hakim", "no_hp": "081234567894", "alamat": "Jl. Panglima Sudirman, Desa Gapurosukolilo, Kec. Gresik"},
    {"nama": "Widya Utama", "no_hp": "081234567895", "alamat": ""},
    {"nama": "Budi Santoso", "no_hp": "081234567896", "alamat": "Jl. Jakarta, Perum GKB, Desa Randuagung, Kec. Kebomas"},
    {"nama": "Fuad Hasan", "no_hp": "081234567897", "alamat": "Jl. KH. Agus Salim, Kel. Karangpohon, Kec. Gresik"},
    {"nama": "Yohannes Siregar", "no_hp": "081234567898", "alamat": "Jl. Raya Manyar, Desa Kompleks Semen Gresik, Kec. Manyar"},
    {"nama": "Mawar Sartika", "no_hp": "081234567899", "alamat": "Jl. Malik Ibrahim, Desa Pekauman, Kec. Gresik"},
    {"nama": "Hendro Utomo", "no_hp": "081234567800", "alamat": "Jl. Jawa, Perum GKB, Kec. Manyar"},
    {"nama": "Aisyah Putri", "no_hp": "081234567801", "alamat": "Jl. Basuki Rahmat, Kec. Gresik"},
    {"nama": "Anwar Sadat", "no_hp": "081234567802", "alamat": ""},
    {"nama": "Dewi Lestari", "no_hp": "081234567803", "alamat": "Jl. Kalimantan, GKB, Kec. Manyar"},
    {"nama": "Eko Prasetyo", "no_hp": "081234567804", "alamat": "Jl. Veteran, Kec. Kebomas"},
]

pendaftaran_siswa = [
        {"nama_siswa": "Ahmad Budi", "status": "Pending", "jenis_kelamin_siswa": "L", "tanggal_lahir_siswa": "2013-05-01", "alamat_siswa": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik", "nama_wali": "Ortu Budi", "no_hp_wali": "081234567890", "alamat_wali": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik", "kelas_id": 2, "foto_kk": "https://drive.google.com/file/d/1HV0NgRtVlKqAqwWPNw0E-eZbX4X-j0-W/view?usp=sharing", "foto_ak": "https://drive.google.com/file/d/1zbgKZ2KS1j68MbNNkNjah4dVruLF2aj2/view?usp=sharing", "foto_pas": "https://drive.google.com/file/d/160KavFZ299JmMnj15ULIl25QW8VWVenB/view?usp=drive_link"},
    {"nama_siswa": "Burhanuddin", "status": "Pending", "jenis_kelamin_siswa": "L", "tanggal_lahir_siswa": "2014-03-09", "alamat_siswa": "Jl. Dr Sutomo, Kel. Tlogopatut, Kec. Gresik", "nama_wali": "Abdul", "no_hp_wali": "081122334455", "alamat_wali": "Jl. Dr Sutomo, Kel. Tlogopatut, Kec. Gresik", "kelas_id": 3, "foto_kk": "https://drive.google.com/file/d/1HV0NgRtVlKqAqwWPNw0E-eZbX4X-j0-W/view?usp=sharing", "foto_ak": "https://drive.google.com/file/d/1zbgKZ2KS1j68MbNNkNjah4dVruLF2aj2/view?usp=sharing", "foto_pas": "https://drive.google.com/file/d/160KavFZ299JmMnj15ULIl25QW8VWVenB/view?usp=drive_link"},
    {"nama_siswa": "Kamal Mohammad", "status": "Pending", "jenis_kelamin_siswa": "L", "tanggal_lahir_siswa": "2013-03-10", "alamat_siswa": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik", "nama_wali": "Kamal", "no_hp_wali": "088866442211", "alamat_wali": "Jl. Dr Sutomo, Kel. Tlogopatut, Kec. Gresik", "kelas_id": 3, "foto_kk": "https://drive.google.com/file/d/1HV0NgRtVlKqAqwWPNw0E-eZbX4X-j0-W/view?usp=sharing", "foto_ak": "https://drive.google.com/file/d/1zbgKZ2KS1j68MbNNkNjah4dVruLF2aj2/view?usp=sharing", "foto_pas": "https://drive.google.com/file/d/160KavFZ299JmMnj15ULIl25QW8VWVenB/view?usp=drive_link"},
]

siswa = [
    {"nama": "Vina Wira", "jenis_kelamin": "P", "tanggal_lahir": "2013-06-02", "alamat": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik", "wali_id": 1, "kelas_id": 2, "pendaftaran_siswa_id": 0},
    {"nama": "Junaidi Zulfikar", "jenis_kelamin": "L", "tanggal_lahir": "2010-08-12", "alamat": "", "wali_id": 2, "kelas_id": 3, "pendaftaran_siswa_id": 0},
    {"nama": "Ahmad Sutrisno", "jenis_kelamin": "L", "tanggal_lahir": "2013-01-02", "alamat": "Jl. Sunan Giri, Desa Giri, Kec. Kebomas", "wali_id": 3, "kelas_id": 2, "pendaftaran_siswa_id": 0},
    {"nama": "Sumiati Siti", "jenis_kelamin": "P", "tanggal_lahir": "2010-12-09", "alamat": "Jl. Dr. Sutomo, Kel. Tlogopatut, Kec. Gresik", "wali_id": 4, "kelas_id": 2, "pendaftaran_siswa_id": 0},
    {"nama": "Wira Rahman", "jenis_kelamin": "L", "tanggal_lahir": "2013-06-23", "alamat": "Jl. Panglima Sudirman, Desa Gapurosukolilo, Kec. Gresik", "wali_id": 5, "kelas_id": 2, "pendaftaran_siswa_id": 0},
    {"nama": "Reza Widya", "jenis_kelamin": "L", "tanggal_lahir": "2016-06-23", "alamat": "", "wali_id": 6, "kelas_id": 1, "pendaftaran_siswa_id": 0},
    {"nama": "Dwi Budi", "jenis_kelamin": "L", "tanggal_lahir": "2016-05-08", "alamat": "Jl. Jakarta, Perum GKB, Desa Randuagung, Kec. Kebomas", "wali_id": 7, "kelas_id": 1, "pendaftaran_siswa_id": 0},
    {"nama": "Amir Fuad", "jenis_kelamin": "L", "tanggal_lahir": "2016-02-18", "alamat": "Jl. KH. Agus Salim, Kel. Karangpohon, Kec. Gresik", "wali_id": 8, "kelas_id": 1},
    {"nama": "Purnama Yohannes", "jenis_kelamin": "L", "tanggal_lahir": "2009-09-04", "alamat": "Jl. Raya Manyar, Desa Kompleks Semen Gresik, Kec. Manyar", "wali_id": 9, "kelas_id": 3, "pendaftaran_siswa_id": 0},
    {"nama": "Daud Mawar", "jenis_kelamin": "P", "tanggal_lahir": "2010-09-24", "alamat": "Jl. Malik Ibrahim, Desa Pekauman, Kec. Gresik", "wali_id": 10, "kelas_id": 3, "pendaftaran_siswa_id": 0},
    {"nama": "Roni Hendro", "jenis_kelamin": "L", "tanggal_lahir": "2015-04-11", "alamat": "Jl. Jawa, Perum GKB, Kec. Manyar", "wali_id": 11, "kelas_id": 1, "pendaftaran_siswa_id": 0},
    {"nama": "Siti Aisyah", "jenis_kelamin": "P", "tanggal_lahir": "2014-11-22", "alamat": "Jl. Basuki Rahmat, Kec. Gresik", "wali_id": 12, "kelas_id": 2, "pendaftaran_siswa_id": 0},
    {"nama": "Fahri Anwar", "jenis_kelamin": "L", "tanggal_lahir": "2012-07-05", "alamat": "", "wali_id": 13, "kelas_id": 3, "pendaftaran_siswa_id": 0},
    {"nama": "Nadia Dewi", "jenis_kelamin": "P", "tanggal_lahir": "2016-01-30", "alamat": "Jl. Kalimantan, GKB, Kec. Manyar", "wali_id": 14, "kelas_id": 1, "pendaftaran_siswa_id": 0},
    {"nama": "Ilham Eko", "jenis_kelamin": "L", "tanggal_lahir": "2011-03-14", "alamat": "Jl. Veteran, Kec. Kebomas", "wali_id": 15, "kelas_id": 3, "pendaftaran_siswa_id": 0},
]

biodata_user = [
    {"meta_role": "Pengajar", "user_id": 1, "nama_lengkap": "Ustadz Ahmad Pengajar", "nama_panggilan": "Ahmad", "jenis_kelamin": "L", "kelas_id": 1, "no_hp": "085111222333", "alamat": "Gresik", "status": "Aktif"},
    {"meta_role": "Pengajar", "user_id": 2, "nama_lengkap": "Ustadzah Siti Pengajar", "nama_panggilan": "Siti", "jenis_kelamin": "P", "kelas_id": 2, "no_hp": "085111222444", "alamat": "Kebomas", "status": "Aktif"},
    {"meta_role": "Pengajar", "user_id": 3, "nama_lengkap": "Ustadz Muhammad Fauzi", "nama_panggilan": "Fauzi", "jenis_kelamin": "L", "kelas_id": 3, "no_hp": "085111222555", "alamat": "Manyar", "status": "Aktif"},
    {"meta_role": "Pengajar", "user_id": 4, "nama_lengkap": "Ustadzah Fatimah Azzahra", "nama_panggilan": "Fatimah", "jenis_kelamin": "P", "kelas_id": 1, "no_hp": "085111222666", "alamat": "Gresik", "status": "Aktif"},
    {"meta_role": "Pengajar", "user_id": 5, "nama_lengkap": "Ustadz Ali Imran", "nama_panggilan": "Ali", "jenis_kelamin": "L", "kelas_id": 2, "no_hp": "085111222777", "alamat": "Kebomas", "status": "Aktif"},
    {"meta_role": "Bendahara", "user_id": 1, "nama_lengkap": "Hani Bendahara", "nama_panggilan": "Hani", "jenis_kelamin": "P", "kelas_id": None, "no_hp": "085111222888", "alamat": "Manyar", "status": "Aktif"},
    {"meta_role": "Bendahara", "user_id": 2, "nama_lengkap": "Rina Amalia", "nama_panggilan": "Rina", "jenis_kelamin": "P", "kelas_id": None, "no_hp": "085111222999", "alamat": "Gresik", "status": "Aktif"}
]

trg_log_siswa = [
    {"siswa_id": 1, "kategori_penilaian": "Bacaan Jilid", "lulus_ulang": "Lulus", "tanggal": "2026-05-10"},
    {"siswa_id": 3, "kategori_penilaian": "Hafalan Doa", "lulus_ulang": "Ulang", "tanggal": "2026-05-11"},
    {"siswa_id": 6, "kategori_penilaian": "Bacaan Jilid", "lulus_ulang": "Lulus", "tanggal": "2026-05-12"},
    {"siswa_id": 9, "kategori_penilaian": "Hafalan Surat", "lulus_ulang": "Lulus", "tanggal": "2026-05-12"},
    {"siswa_id": 12, "kategori_penilaian": "Hafalan Doa", "lulus_ulang": "Lulus", "tanggal": "2026-05-13"},
    {"siswa_id": 15, "kategori_penilaian": "Bacaan Jilid", "lulus_ulang": "Ulang", "tanggal": "2026-05-14"},
]

spp_siswa = [
    {"siswa_id": 1, "status": "Lunas", "tanggal": "2026-05-01", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 2, "status": "Belum Lunas", "tanggal": "2026-05-02", "pembayaran": 50000, "sisa": 100000},
    {"siswa_id": 3, "status": "Lunas", "tanggal": "2026-05-02", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 4, "status": "Lunas", "tanggal": "2026-05-03", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 5, "status": "Belum Lunas", "tanggal": "2026-05-04", "pembayaran": 0, "sisa": 150000},
    {"siswa_id": 6, "status": "Lunas", "tanggal": "2026-05-04", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 7, "status": "Lunas", "tanggal": "2026-05-05", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 8, "status": "Belum Lunas", "tanggal": "2026-05-05", "pembayaran": 75000, "sisa": 75000},
    {"siswa_id": 9, "status": "Lunas", "tanggal": "2026-05-06", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 10, "status": "Lunas", "tanggal": "2026-05-06", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 11, "status": "Lunas", "tanggal": "2026-05-07", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 12, "status": "Belum Lunas", "tanggal": "2026-05-07", "pembayaran": 0, "sisa": 150000},
    {"siswa_id": 13, "status": "Lunas", "tanggal": "2026-05-08", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 14, "status": "Lunas", "tanggal": "2026-05-08", "pembayaran": 150000, "sisa": 0},
    {"siswa_id": 15, "status": "Belum Lunas", "tanggal": "2026-05-09", "pembayaran": 50000, "sisa": 100000},
]

gaji_pengajar = [
    {"biodata_user_id": 1, "tanggal_gaji": "2026-05-25", "gaji": 1200000, "status": "Sudah digaji"},
    {"biodata_user_id": 2, "tanggal_gaji": "2026-05-25", "gaji": 1200000, "status": "Sudah digaji"},
    {"biodata_user_id": 3, "tanggal_gaji": "2026-05-25", "gaji": 1250000, "status": "Sudah digaji"},
    {"biodata_user_id": 4, "tanggal_gaji": "2026-05-25", "gaji": 1150000, "status": "Belum digaji"},
    {"biodata_user_id": 5, "tanggal_gaji": "2026-05-25", "gaji": 1150000, "status": "Belum digaji"},
]

pengganti_pengajar = [
    {"pengajar_id": 1, "pengganti_pengajar_id": 2, "kelas_id": 1, "tanggal": "2026-05-12T14:00:00", "note": "Menggantikan karena sakit"},
    {"pengajar_id": 3, "pengganti_pengajar_id": 5, "kelas_id": 3, "tanggal": "2026-05-15T15:30:00", "note": "Ada keperluan keluarga"},
]

trg_transaksi = [
    {"kategori": "Pemasukan", "tanggal": "2026-05-01", "nama": "Pembayaran SPP Vina Wira", "nominal": 150000, "spp_siswa_id": 1, "gaji_pengajar_id": None, "note": "SPP Mei"},
    {"kategori": "Pemasukan", "tanggal": "2026-05-02", "nama": "Pembayaran SPP Ahmad Sutrisno", "nominal": 150000, "spp_siswa_id": 3, "gaji_pengajar_id": None, "note": "SPP Mei"},
    {"kategori": "Pemasukan", "tanggal": "2026-05-03", "nama": "Pembayaran SPP Sumiati Siti", "nominal": 150000, "spp_siswa_id": 4, "gaji_pengajar_id": None, "note": "SPP Mei"},
    {"kategori": "Pemasukan", "tanggal": "2026-05-04", "nama": "Pembayaran SPP Reza Widya", "nominal": 150000, "spp_siswa_id": 6, "gaji_pengajar_id": None, "note": "SPP Mei"},
    {"kategori": "Pengeluaran", "tanggal": "2026-05-25", "nama": "Gaji Ustadz Ahmad", "nominal": 1200000, "spp_siswa_id": None, "gaji_pengajar_id": 1, "note": "Gaji Mei"},
    {"kategori": "Pengeluaran", "tanggal": "2026-05-25", "nama": "Gaji Ustadzah Siti", "nominal": 1200000, "spp_siswa_id": None, "gaji_pengajar_id": 2, "note": "Gaji Mei"},
    {"kategori": "Pengeluaran", "tanggal": "2026-05-25", "nama": "Gaji Ustadz Muhammad Fauzi", "nominal": 1250000, "spp_siswa_id": None, "gaji_pengajar_id": 3, "note": "Gaji Mei"},
]

penilaian_surat = [
    {"siswa_id": 1, "nama_surat": "An-Naba", "tanggal_setor": "2026-05-10", "kelancaran": 85, "ketepatan_bacaan": 80, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "LULUS", "note": "Lancar"},
    {"siswa_id": 5, "nama_surat": "An-Naziat", "tanggal_setor": "2026-05-11", "kelancaran": 70, "ketepatan_bacaan": 75, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "ULANG", "note": "Murajaah lagi di rumah"},
    {"siswa_id": 9, "nama_surat": "Abasa", "tanggal_setor": "2026-05-12", "kelancaran": 90, "ketepatan_bacaan": 95, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "LULUS", "note": "Excellent makhraj"},
    {"siswa_id": 13, "nama_surat": "Al-Infitar", "tanggal_setor": "2026-05-13", "kelancaran": 80, "ketepatan_bacaan": 80, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "LULUS", "note": "Bagus"},
]

penilaian_doa = [
    {"siswa_id": 2, "nama_doa": "Doa Makan", "tanggal_setor": "2026-05-10", "nilai": 90, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Bagus"},
    {"siswa_id": 7, "nama_doa": "Doa Tidur", "tanggal_setor": "2026-05-11", "nilai": 85, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Lancar"},
    {"siswa_id": 12, "nama_doa": "Doa Masuk Masjid", "tanggal_setor": "2026-05-12", "nilai": 60, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Ulang", "note": "Belum hafal akhir doa"},
    {"siswa_id": 14, "nama_doa": "Doa Keluar Rumah", "tanggal_setor": "2026-05-13", "nilai": 95, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Sangat baik"},
]

penilaian_jilid = [
    {"siswa_id": 3, "materi_bacaan": "Halaman 10", "tanggal_setor": "2026-05-10", "nilai_tajwid": 75, "nilai_makhraj": 70, "nilai_kelancaran": 80, "nilai_akhir": 75, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Perhatikan panjang pendek"},
    {"siswa_id": 6, "materi_bacaan": "Halaman 15", "tanggal_setor": "2026-05-11", "nilai_tajwid": 85, "nilai_makhraj": 80, "nilai_kelancaran": 85, "nilai_akhir": 83, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Naik halaman"},
    {"siswa_id": 8, "materi_bacaan": "Halaman 3", "tanggal_setor": "2026-05-12", "nilai_tajwid": 65, "nilai_makhraj": 60, "nilai_kelancaran": 70, "nilai_akhir": 65, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Ulang", "note": "Ulangi halaman ini besok"},
    {"siswa_id": 11, "materi_bacaan": "Halaman 22", "tanggal_setor": "2026-05-13", "nilai_tajwid": 80, "nilai_makhraj": 75, "nilai_kelancaran": 80, "nilai_akhir": 78, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Lulus", "note": "Lancar"},
    {"siswa_id": 15, "materi_bacaan": "Halaman 5", "tanggal_setor": "2026-05-14", "nilai_tajwid": 70, "nilai_makhraj": 65, "nilai_kelancaran": 70, "nilai_akhir": 68, 
     # "waktu_penilaian": "Harian", 
     "lulus_ulang": "Ulang", "note": "Makhraj huruf 'tsa' masih keliru"},
]

ENTITY_REGISTRY = [
    {
        "name": "User Admin",
        "create_endpoint": f"{BASE_URL}/auth/register/",
        "delete_endpoint": f"{BASE_URL}/auth/",
        "data": admin,
        "is_auth_route": True
    },
    {
        "name": "User Pengajar",
        "create_endpoint": f"{BASE_URL}/auth/register/",
        "delete_endpoint": f"{BASE_URL}/auth/",
        "data": pengajar,
        "is_auth_route": True
    },
    {
        "name": "User Bendahara",
        "create_endpoint": f"{BASE_URL}/auth/register/",
        "delete_endpoint": f"{BASE_URL}/auth/",
        "data": bendahara,
        "is_auth_route": True
    },
    {
        "name": "Kelas",
        "endpoint": f"{BASE_URL}/kelas/",
        "data": kelas,
        "is_auth_route": False
    },
    {
        "name": "Wali Murid",
        "endpoint": f"{BASE_URL}/wali/",
        "data": wali,
        "is_auth_route": False
    },
    {
        "name": "Pendaftaran Siswa",
        "endpoint": f"{BASE_URL}/pendaftaran-siswa/",
        "data": pendaftaran_siswa,
        "is_auth_route": False
    },
    {
        "name": "Siswa",
        "endpoint": f"{BASE_URL}/siswa/",
        "data": siswa,
        "is_auth_route": False
    },
    {"name": "Biodata User", "endpoint": f"{BASE_URL}/biodata-user/", "data": biodata_user, "is_auth_route": False},
    {"name": "Trg Log Siswa", "endpoint": f"{BASE_URL}/trg-log-siswa/", "data": trg_log_siswa, "is_auth_route": False},
    {"name": "SPP Siswa", "endpoint": f"{BASE_URL}/spp-siswa/", "data": spp_siswa, "is_auth_route": False},
    {"name": "Gaji Pengajar", "endpoint": f"{BASE_URL}/gaji-pengajar/", "data": gaji_pengajar, "is_auth_route": False},
    {"name": "Pengganti Pengajar", "endpoint": f"{BASE_URL}/pengganti-pengajar/", "data": pengganti_pengajar, "is_auth_route": False},
    {"name": "Trg Transaksi", "endpoint": f"{BASE_URL}/trg-transaksi/", "data": trg_transaksi, "is_auth_route": False},
    {"name": "Penilaian Surat", "endpoint": f"{BASE_URL}/penilaian-surat/", "data": penilaian_surat, "is_auth_route": False},
    {"name": "Penilaian Doa", "endpoint": f"{BASE_URL}/penilaian-doa/", "data": penilaian_doa, "is_auth_route": False},
    {"name": "Penilaian Jilid", "endpoint": f"{BASE_URL}/penilaian-jilid/", "data": penilaian_jilid, "is_auth_route": False},
    # {
    #     "name": "name",
    #     "endpoint": f"{BASE_URL}/route/",
    #     "data": data,
    #     "is_auth_route": False
    # }
]

def get_target_url(entity: dict, operation: str) -> str | None:
    """Mengembalikan URL yang sesuai berdasarkan jenis operasi (create/delete/get)"""
    if operation == "create":
        return entity.get("create_endpoint") or entity.get("endpoint")
    
    return entity.get("delete_endpoint") or entity.get("endpoint")

def login_session(session: requests.Session, username: str, password: str) -> bool:
    """Melakukan login untuk menanam HTTP-Only Cookie JWT ke object Session"""
    print(f"Authenticating as {username}... ", end="")
    payload = {"username": username, "password": password}
    res = session.post(f"{BASE_URL}/auth/login/", json=payload)
    if res.status_code == 200:
        print("SUCCESS")
        return True
    print("FAILED")
    return False

def create_all_data(session: requests.Session):
    """Create all data in sequentially"""
    print("=== START SEEDING PROCESS ===\n")
    
    identity_map = {}

    for entity in ENTITY_REGISTRY:
        if not entity["is_auth_route"]:
            authenticated = login_session(session, "admin1", "admin1234")
            if not authenticated:
                print(f"Aborting {entity['name']} seeding due to authentication failure.")
                continue

        print(f"\n[Seeding Entitas: {entity['name']}]")

        url = get_target_url(entity, "create")
        if not url:
            print("Error: Cannot get (create/delete/get) url")
            exit(1)

        identity_map[entity["name"]] = {}

        for index, item in enumerate(entity["data"]):
            if entity["name"] == "Siswa":
                item["wali_id"] = identity_map.get("Wali Murid", {}).get(item["wali_id"] - 1)
                item["kelas_id"] = identity_map.get("Kelas", {}).get(item["kelas_id"] - 1)
            
            elif entity["name"] == "Biodata User":
                target_role = item.pop("meta_role", "Pengajar")
                item["user_id"] = identity_map.get(f"User {target_role}", {}).get(item["user_id"] - 1)
                if item.get("kelas_id"):
                    item["kelas_id"] = identity_map.get("Kelas", {}).get(item["kelas_id"] - 1)

            elif entity["name"] in ["Trg Log Siswa", "SPP Siswa", "Penilaian Surat", "Penilaian Doa", "Penilaian Jilid"]:
                item["siswa_id"] = identity_map.get("Siswa", {}).get(item["siswa_id"] - 1)

            elif entity["name"] == "Gaji Pengajar":
                item["biodata_user_id"] = identity_map.get("Biodata User", {}).get(item["biodata_user_id"] - 1)

            elif entity["name"] == "Pengganti Pengajar":
                item["pengajar_id"] = identity_map.get("User Pengajar", {}).get(item["pengajar_id"] - 1)
                item["pengganti_pengajar_id"] = identity_map.get("User Pengajar", {}).get(item["pengganti_pengajar_id"] - 1)
                item["kelas_id"] = identity_map.get("Kelas", {}).get(item["kelas_id"] - 1)

            elif entity["name"] == "Trg Transaksi":
                if item.get("spp_siswa_id"):
                    item["spp_siswa_id"] = identity_map.get("SPP Siswa", {}).get(item["spp_siswa_id"] - 1)
                if item.get("gaji_pengajar_id"):
                    item["gaji_pengajar_id"] = identity_map.get("Gaji Pengajar", {}).get(item["gaji_pengajar_id"] - 1)


            identifier = item.get("username") or item.get("nama") or item.get("nama_lengkap") or item.get("nama_surat") or item.get("materi_bacaan") or f"Index-{index}"
            print(f"-> Creating {entity['name']}: {identifier}... ", end="")
            
            res = session.post(url, json=item)
            if res.status_code in [200, 201]:
                print("SUCCESS")
                res_data = res.json()
                if "id" in res_data:
                    identity_map[entity["name"]][index] = res_data["id"]
            else:
                print("FAILED")
                try:
                    error_detail = res.json().get('detail', res.text)
                    print(f"   Detail (JSON): {error_detail}")
                except Exception:
                    print(f"   Status Code: {res.status_code}")
                    print(f"   Raw Response: {res.text}")

def delete_all_data(session: requests.Session):
    """
    Delete data in reversed order (from child to parent) to avoid constraint error
    """
    print("=== START PURGING PROCESS ===\n")
    
    if not login_session(session, "admin1", "admin1234"):
        print("Aborting wipe operation due to auth failure.")
        return

    for entity in reversed(ENTITY_REGISTRY):
        print(f"\n[Purging Entity: {entity['name']}]")
        
        base_url = get_target_url(entity, "delete")
        if not base_url:
            print("Error: Cannot get (create/delete/get) url")
            exit(1)

        get_res = session.get(base_url)
        if get_res.status_code != 200:
            print(f"-> Failed to take data {entity['name']}: {get_res.text}")
            continue

        items = get_res.json()
        for item in items:
            target_id = item["id"]
            target_name = item.get("username") or item.get("nama") or item.get("nama_lengkap") or f"ID-{target_id}"
            print(f"-> Deleting ({target_id}) {target_name}... ", end="")
            
            delete_url = f"{base_url}{target_id}" if base_url.endswith("/") else f"{base_url}/{target_id}"

            del_res = session.delete(delete_url)
            if del_res.status_code == 200:
                print("SUCCESS")
            else:
                print("FAILED")
                print(f"   Detail: {del_res.json().get('detail', del_res.text)}")

def print_usage():
    print(f"""Error: Missing or invalid argument!
Usage:
    python {sys.argv[0]} create
    # OR
    python {sys.argv[0]} delete""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    session = requests.Session()

    if sys.argv[1] == "create":
        create_all_data(session)
    elif sys.argv[1] == "delete":
        delete_all_data(session)
    else:
        print_usage()
        sys.exit(1)
