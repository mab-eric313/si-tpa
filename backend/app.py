import fastapi as fa
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), "static")

templates = Jinja2Templates(directory="frontend")


@app.get("/")
async def root(request: fa.Request):
    return templates.TemplateResponse(
            request, "index.html", context={"request": request}
    )
