from pathlib import Path
from dotenv import load_dotenv
import getpass
import keyring
import os
import ssl

load_dotenv()

SERVICE_NAME = "si-tpa_db"
password = keyring.get_password(SERVICE_NAME, os.getenv("DB_USER", ""))

def get_password() -> str:
    password = getpass.getpass("enter your DB password: ")
    keyring.set_password(SERVICE_NAME, os.getenv("DB_USER", ""), password)

    return password

if not os.getenv("DB_PASS") and not password:
    password = get_password()

DB_CONNECTION = os.getenv("DB_CONNECTION")
DB_NAME       = os.getenv("DB_NAME")
DB_USER       = os.getenv("DB_USER")
DB_HOST       = os.getenv("DB_HOST")
DB_PORT       = os.getenv("DB_PORT")
DB_PASS       = os.getenv("DB_PASS", password)
DB_USE_SSL    = os.getenv("DB_USE_SSL", "false").lower() == "true"

connect_args = {}

if DB_USE_SSL:
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    connect_args["ssl"] = ssl_context

DB_URL = f"{DB_CONNECTION}+asyncmy://" \
         f"{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

BASE_DB_URL =  f"{DB_CONNECTION}+asyncmy://" \
            f"{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}"

SECRET_KEY = os.getenv("SECRET_KEY", "")

os.environ["PYTHONPATH"] = str(Path(__file__).resolve().parents[0])
os.environ["DB_URL"] = DB_URL

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTE = 60

PUBLIC_FRONTEND_BASE_URL = os.getenv("PUBLIC_FRONTEND_BASE_URL", "")
