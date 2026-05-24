from .models.data import Siswa
from .models import data


def get_all() -> list[Siswa]:
    return data.get_all()

def get_one(user_id: int) -> data.Siswa | None:
    return data.get_one(user_id)

def create(siswa: Siswa) -> Siswa:
    """Create siswa"""
    return data.create(siswa)

def modify(user_id: int, siswa: Siswa) -> Siswa:
    """Partially modify siswa"""
    return data.modify(user_id, siswa)

# TODO: (MEDIUM) replace query currently is not available
# def replace(user_id: int, siswa: model.Siswa) -> model.Siswa:
#     return siswa

def delete(user_id: int) -> bool:
    return data.delete(user_id)
