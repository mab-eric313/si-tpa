import os
import ssl
import cloudinary
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SERVICE_NAME = "si-tpa_db"
DB_USER = os.getenv("DB_USER", "")

DB_PASS = os.getenv("DB_PASS")

if not DB_PASS:
    try:
        import keyring
        DB_PASS = keyring.get_password(SERVICE_NAME, DB_USER)
    except Exception:
        DB_PASS = None

if not DB_PASS:
    raise ValueError(
        "DB_PASS tidak ditemukan! \n"
        "1. Untuk Cloud Deployment: Jalankan 'fastapi cloud env set --secret DB_PASS \"password_anda\"'\n"
        "2. Untuk Local Development: Pastikan password tersimpan di keyring atau tambahkan DB_PASS ke file .env"
    )

DB_CONNECTION = os.getenv("DB_CONNECTION")
DB_NAME       = os.getenv("DB_NAME")
DB_HOST       = os.getenv("DB_HOST")
DB_PORT       = os.getenv("DB_PORT")
DB_USE_SSL    = os.getenv("DB_USE_SSL", "false").lower() == "true"

connect_args = {}

if DB_USE_SSL:
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    connect_args["ssl"] = ssl_context

DB_URL = f"{DB_CONNECTION}+asyncmy://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
BASE_DB_URL = f"{DB_CONNECTION}+asyncmy://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}"

SECRET_KEY = os.getenv("SECRET_KEY", "")

os.environ["PYTHONPATH"] = str(Path(__file__).resolve().parents[0])
os.environ["DB_URL"] = DB_URL

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTE = 60

PUBLIC_FRONTEND_BASE_URL = os.getenv("PUBLIC_FRONTEND_BASE_URL", "")

# Cloudinary
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

cloudinary.config( 
    cloud_name = CLOUDINARY_CLOUD_NAME, 
    api_key = CLOUDINARY_API_KEY, 
    api_secret = CLOUDINARY_API_SECRET,
    secure=True
)

