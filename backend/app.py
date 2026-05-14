# The backend is still not yet ready

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello() -> dict:
    return {"hello":  "world"}
