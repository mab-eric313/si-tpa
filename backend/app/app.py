from fastapi import FastAPI
from app.database import Base, engine
from app.routers import siswa

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(siswa.router)

@app.get("/")
def hello():
    return {"hello": "world"}
