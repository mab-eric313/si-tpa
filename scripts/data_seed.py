"""
Take note this file is for development only

The purpose of this file is to create an users, so you can login using this
pre-configured username and password.

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
    {"username": "admin1", "password": "admin1234", "role": "admin"},
]

pengajar = [
    {"username": "pengajar1", "password": "pengajar1234", "role": "pengajar"},
    {"username": "pengajar2", "password": "pengajar1234", "role": "pengajar"}
]

bendahara = [
    {"username": "bendahara1", "password": "bendahara1234", "role": "bendahara"},
    {"username": "bendahara2", "password": "bendahara1234", "role": "bendahara"}
]

kelas = [
    {"nama": "jilid_1-3"},
    {"nama": "jilid_4-6"},
    {"nama": "alquran"},
]

siswa = [
    {
        "nama": "Vina Wira", "jenis_kelamin": "P", "tanggal_lahir": "2013-06-02", 
        "alamat": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik", 
        "wali_id": 1, "kelas_id": 2
    },
    {
        "nama": "Junaidi Zulfikar", "jenis_kelamin": "L", "tanggal_lahir": "2010-08-12", 
        "alamat": "", 
        "wali_id": 2, "kelas_id": 3
    },
    {
        "nama": "Ahmad Sutrisno", "jenis_kelamin": "L", "tanggal_lahir": "2013-01-02", 
        "alamat": "Jl. Sunan Giri, Desa Giri, Kec. Kebomas", 
        "wali_id": 3, "kelas_id": 2
    },
    {
        "nama": "Sumiati Siti", "jenis_kelamin": "P", "tanggal_lahir": "2010-12-09", 
        "alamat": "Jl. Dr. Sutomo, Kel. Tlogopatut, Kec. Gresik", 
        "wali_id": 4, "kelas_id": 2
    },
    {
        "nama": "Wira Rahman", "jenis_kelamin": "L", "tanggal_lahir": "2013-06-23", 
        "alamat": "Jl. Panglima Sudirman, Desa Gapurosukolilo, Kec. Gresik", 
        "wali_id": 5, "kelas_id": 2
    },
    {
        "nama": "Reza Widya", "jenis_kelamin": "L", "tanggal_lahir": "2016-06-23", 
        "alamat": "", 
        "wali_id": 6, "kelas_id": 1
    },
    {
        "nama": "Dwi Budi", "jenis_kelamin": "L", "tanggal_lahir": "2016-05-08", 
        "alamat": "Jl. Jakarta, Perum GKB, Desa Randuagung, Kec. Kebomas", 
        "wali_id": 7, "kelas_id": 1
    },
    {
        "nama": "Amir Fuad", "jenis_kelamin": "L", "tanggal_lahir": "2016-02-18", 
        "alamat": "Jl. KH. Agus Salim, Kel. Karangpohon, Kec. Gresik", 
        "wali_id": 8, "kelas_id": 1
    },
    {
        "nama": "Purnama Yohannes", "jenis_kelamin": "L", "tanggal_lahir": "2009-09-04", 
        "alamat": "Jl. Raya Manyar, Desa Kompleks Semen Gresik, Kec. Manyar", 
        "wali_id": 9, "kelas_id": 3
    },
    {
        "nama": "Daud Mawar", "jenis_kelamin": "P", "tanggal_lahir": "2010-09-24", 
        "alamat": "Jl. Malik Ibrahim, Desa Pekauman, Kec. Gresik", 
        "wali_id": 10, "kelas_id": 3
    },
]

wali = [
    {
        "nama": "Budi Wibowo", "no_hp": "", 
        "alamat": "Jl. Raden Santri, Desa Bedilan, Kec. Gresik"
    },
    {
        "nama": "Zulfikar Hasan", "no_hp": "XXXXXXXXXXXX", 
        "alamat": ""
    },
    {
        "nama": "Sutrisno Hadi", "no_hp": "XXXXXXXXXXXX", 
        "alamat": "Jl. Sunan Giri, Desa Giri, Kec. Kebomas"
    },
    {
        "nama": "Siti Aminah", "no_hp": "", 
        "alamat": "Jl. Dr. Sutomo, Kel. Tlogopatut, Kec. Gresik"
    },
    {
        "nama": "Rahman Hakim", "no_hp": "XXXXXXXXXXXX", 
        "alamat": "Jl. Panglima Sudirman, Desa Gapurosukolilo, Kec. Gresik"
    },
    {
        "nama": "Widya Utama", "no_hp": "XXXXXXXXXXXX", 
        "alamat": ""
    },
    {
        "nama": "Budi Santoso", "no_hp": "", 
        "alamat": "Jl. Jakarta, Perum GKB, Desa Randuagung, Kec. Kebomas"
    },
    {
        "nama": "Fuad Hasan", "no_hp": "XXXXXXXXXXXX", 
        "alamat": "Jl. KH. Agus Salim, Kel. Karangpohon, Kec. Gresik"
    },
    {
        "nama": "Yohannes Siregar", "no_hp": "XXXXXXXXXXXX", 
        "alamat": "Jl. Raya Manyar, Desa Kompleks Semen Gresik, Kec. Manyar"
    },
    {
        "nama": "Mawar Sartika", "no_hp": "", 
        "alamat": "Jl. Malik Ibrahim, Desa Pekauman, Kec. Gresik"
    },
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
        "name": "Siswa",
        "endpoint": f"{BASE_URL}/siswa/",
        "data": siswa,
        "is_auth_route": False
    },
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
            authenticated = login_session(session, "pengajar1", "pengajar1234")
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
                old_wali_index = item["wali_id"] - 1 
                real_wali_id = identity_map.get("Wali Murid", {}).get(old_wali_index)
                if real_wali_id:
                    item["wali_id"] = real_wali_id
                else:
                    print(f"-> Skipping {item['nama']}: Real Wali ID tidak ditemukan (Seeding Wali gagal/terlewat).")
                    continue
                
                old_kelas_idx = item["kelas_id"] - 1
                real_kelas_id = identity_map.get("Kelas", {}).get(old_kelas_idx)
                if real_kelas_id:
                    item["kelas_id"] = real_kelas_id
                else:
                    print(f"-> Skipping {item['nama']}: Kelas ID gagal dipetakan.")
                    continue

            identifier = item.get("username") or item.get("nama")
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
            target_name = item.get("username") or item.get("nama")
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
