from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), "static")

templates = Jinja2Templates(directory="frontend")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
            request, "index.html", context={"request": request}
    )


@app.get("/static/html/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse(
            request, "dashboard.html", {"request": request}
    )


@app.get("/static/html/data-siswa")
async def data_siswa(request: Request):
    return templates.TemplateResponse(
            request, "data-siswa.html", {"request": request}
    )


@app.get("/static/html/absensi")
async def absensi(request: Request):
    return templates.TemplateResponse(
            request, "absensi.html", {"request": request}
    )


@app.get("/static/html/keuangan")
async def keuangan(request: Request):
    return templates.TemplateResponse(
            request, "keuangan.html", {"request": request}
    )


@app.get("/static/html/laporan-akademik")
async def laporan_akademik(request: Request):
    return templates.TemplateResponse(
            request, "laporan-akademik.html", {"request": request}
    )


@app.get("/static/html/jadwal")
async def jadwal(request: Request):
    return templates.TemplateResponse(
            request, "jadwal.html", {"request": request}
    )
