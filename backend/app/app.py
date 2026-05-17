from fastapi import FastAPI
from . import web

app = FastAPI()

app.include_router(web.router)

@app.get("/")
def hello():
    return {"hello": "world"}
