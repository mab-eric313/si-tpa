from fastapi import APIRouter
from app.models.data import Siswa
from app.models.tables import SiswaBaseResponse
from . import service


router = APIRouter(prefix="/siswa")

@router.get("", response_model=SiswaBaseResponse)
@router.get("/", response_model=SiswaBaseResponse)
def get_all() -> list[SiswaBaseResponse]:
    return service.get_all()

@router.get("/{user_id}", response_model=SiswaBaseResponse)
def get_one() -> SiswaBaseResponse:
    siswa = Siswa(
        id=1,
        nama="budi",
        jenis_kelamin="L",
        tanggal_lahir="2026-05-24",
        alamat="Indo",
        wali_id=11,
        kelas_id=111,
    )
    pydantic_siswa = SiswaBaseResponse.model_validate(siswa)
    return pydantic_siswa

@router.post("", response_model=SiswaBaseResponse)
@router.post("/", response_model=SiswaBaseResponse)
def create(siswa: Siswa) -> Siswa:
    """Create siswa"""
    return service.create(siswa)

@router.patch("/", response_model=SiswaBaseResponse)
def modify(user_id: int, siswa: Siswa) -> Siswa:
    """Partially modify siswa"""
    return service.modify(user_id, siswa)

# TODO: (MEDIUM) replace query currently is not available
# @router.put("/")
# def replace(user_id: int, siswa: model.Siswa) -> model.Siswa:
#     return service.replace(user_id, siswa)

@router.delete("/{user_id}", response_model=SiswaBaseResponse)
def delete(user_id: int) -> bool:
    return service.delete(user_id)
