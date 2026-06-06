from fastapi import FastAPI
from app.database import Base, engine
from app.routers import siswa
from app.routers import kelas
from app.routers import wali

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(siswa.router)
app.include_router(kelas.router)
app.include_router(wali.router)

@app.get("")
@app.get("/")
def hello():
    return {"hello": "world"}
