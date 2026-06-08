import config
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import siswa
from app.routers import kelas
from app.routers import wali

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(siswa.router)
app.include_router(kelas.router)
app.include_router(wali.router)

@app.get("")
@app.get("/")
def hello():
    return {"hello": "world"}
