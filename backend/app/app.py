import config # noqa F401
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from app.database import engine
from app.routers import auth
from app.routers import siswa
from app.routers import kelas
from app.routers import wali

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(siswa.router)
app.include_router(kelas.router)
app.include_router(wali.router)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("")
@app.get("/")
async def hello():
    return {"message": "world"}

@app.get("/api/data")
async def read_data():
    return {"message": "hello from fastapi"}
