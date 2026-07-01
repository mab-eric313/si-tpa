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

BASE_URL = "http://localhost:8000/auth"

pengajar = [
    {"username": "pengajar1", "password": "pengajar1234", "role": "pengajar"},
    {"username": "pengajar2", "password": "pengajar1234", "role": "pengajar"}
]

bendahara = [
    {"username": "bendahara1", "password": "bendahara1234", "role": "bendahara"},
    {"username": "bendahara2", "password": "bendahara1234", "role": "bendahara"}
]

admin = [
    {"username": "admin1", "password": "admin1234", "role": "admin"},
]

def login_as_admin(session: requests.Session) -> bool:
    print("Authenticating as admin... ", end="")
    payload = {"username": "admin1", "password": "admin1234"}
    res = session.post(f"{BASE_URL}/login/", json=payload)
    if res.status_code == 200:
        print("SUCCESS")
        return True
    print("FAILED")
    print("Make sure admin1 is registered")
    return False

def create(session: requests.Session, all_users: list):
    res_list = list()
    for user in all_users:
        print(f"Creating user: {user["username"]} ", end="")
        res = session.post(f"{BASE_URL}/register/", json=user)
        if res.status_code == 200:
            print("SUCCESS")
            res_list.append(res)
        else:
            print("FAILED")
            print(f"{res.json().get('detail')}")

    print("\n--- Summary Responses ---")
    for res in res_list:
        print(f"{res.json()}")

def delete(session: requests.Session):
    if not login_as_admin(session):
        print("Aborting delete operation due to auth failure")
        return

    get_all_res = session.get(f"{BASE_URL}/")
    if get_all_res.status_code != 200:
        print(f"Failed to fetch users: {get_all_res.json().get('detail')}")
        return

    users = get_all_res.json()
    for user in users:
        target_user_id = user["id"]
        target_username = user["username"]
        res_list = list()

        print(f"Deleting user: ({target_user_id}) {target_username} ", end="")

        res = session.delete(f"{BASE_URL}/{target_user_id}")
        if res.status_code == 200:
            print("SUCCESS")
            res_list.append(res)
        else:
            print("FAILED")
            print(f"{res.json().get('detail')}")

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

    all_users: list = pengajar + bendahara + admin
    session = requests.Session()

    if sys.argv[1] == "create":
        create(session, all_users)
    elif sys.argv[1] == "delete":
        delete(session)
    else:
        print_usage()
        sys.exit(1)
