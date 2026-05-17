from fastapi import APIRouter
from app.datas.data import Siswa
from . import service


router = APIRouter(prefix="/siswa")

@router.get("")
@router.get("/")
def get_all() -> list[Siswa]:
    return service.get_all()

@router.get("/{user_id}")
def get_one(user_id: int) -> Siswa | None:
    return service.get_one(user_id)

@router.post("")
@router.post("/")
def create(siswa: Siswa) -> Siswa:
    """Create siswa"""
    return service.create(siswa)

@router.patch("/")
def modify(user_id: int, siswa: Siswa) -> Siswa:
    """Partially modify siswa"""
    return service.modify(user_id, siswa)

# TODO: (MEDIUM) replace query currently is not available
# @router.put("/")
# def replace(user_id: int, siswa: model.Siswa) -> model.Siswa:
#     return service.replace(user_id, siswa)

@router.delete("/{user_id}")
def delete(user_id: int) -> bool:
    return service.delete(user_id)
