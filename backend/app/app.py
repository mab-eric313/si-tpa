from app.models.init import Base, engine
from fastapi import FastAPI
from . import web

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(web.router)

@app.get("/")
def hello():
    return {"hello": "world"}
