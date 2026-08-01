import config # noqa F401
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from app.database import engine, create_db_if_not_exists
from app.routers import (
    auth, siswa, kelas, wali, biodata_user, gaji_pengajar, pengganti_pengajar,
    penilaian_doa, penilaian_jilid, penilaian_surat, spp_siswa, trg_log_siswa, 
    trg_transaksi, pendaftaran_siswa, absensi, upload
)

@asynccontextmanager
async def lifespan(_: FastAPI):
    await create_db_if_not_exists(config.BASE_DB_URL, config.DB_NAME)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(siswa.router)
app.include_router(kelas.router)
app.include_router(wali.router)
app.include_router(biodata_user.router)
app.include_router(gaji_pengajar.router)
app.include_router(pengganti_pengajar.router)
app.include_router(penilaian_doa.router)
app.include_router(penilaian_jilid.router)
app.include_router(penilaian_surat.router)
app.include_router(spp_siswa.router)
app.include_router(trg_log_siswa.router)
app.include_router(trg_transaksi.router)
app.include_router(pendaftaran_siswa.router)
app.include_router(absensi.router)
app.include_router(upload.router)

origins = [
    config.PUBLIC_FRONTEND_BASE_URL,
    "https://si-tpa.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.get("")
@app.get("/")
async def hello():
    return {"message": "hello world"}

@app.get("/api/data")
async def read_data():
    return {"message": "hello from fastapi"}
