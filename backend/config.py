from pathlib import Path
from dotenv import load_dotenv
import getpass
import keyring
import os

load_dotenv()

SERVICE_NAME = "si-tpa_db"
password = keyring.get_password(SERVICE_NAME, os.getenv("DB_USER", ""))

def get_password() -> str:
    password = getpass.getpass("enter your DB password: ")
    keyring.set_password(SERVICE_NAME, os.getenv("DB_USER", ""), password)

    return password

if not password:
    password = get_password()

DB_NAME     = os.getenv("DB_NAME")
DB_USER     = os.getenv("DB_USER")
DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_PASSWORD = password

DB_URL = f"mariadb+asyncmy://" \
         f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

BASE_DB_URL =  f"mariadb+asyncmy://" \
            f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

SECRET_KEY = os.getenv("SECRET_KEY", "")

os.environ["PYTHONPATH"] = str(Path(__file__).resolve().parents[0])
os.environ["DB_URL"] = DB_URL

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTE = 60
