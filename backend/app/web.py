from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.tables import Siswa, SiswaResponse, SiswaCreate, SiswaUpdate
from app.models.init import get_session


router = APIRouter(prefix="/siswa")

@router.get("/", response_model=list[SiswaResponse])
def get_all(session: Session = Depends(get_session)) -> list[Siswa]:
    return list(session.scalars(select(Siswa)).all())

@router.get("/{id}", response_model=SiswaResponse)
def get_one(id: int, session: Session = Depends(get_session)):
    siswa = session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    return siswa

@router.post("/", response_model=SiswaResponse)
def create(payload: SiswaCreate, session: Session = Depends(get_session)):
    """Create siswa"""
    siswa = Siswa(**payload.model_dump())
    session.add(siswa)
    session.commit()
    session.refresh(siswa)
    return siswa

@router.patch("/{id}", response_model=SiswaResponse)
def modify(id: int, payload: SiswaUpdate, session: Session = Depends(get_session)):
    """Partially modify siswa"""
    siswa = session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(siswa, key, val)

    session.commit()
    session.refresh(siswa)
    return siswa

@router.delete("/{id}", response_model=SiswaResponse)
def delete(id: int, session: Session = Depends(get_session)):
    siswa = session.get(Siswa, id)
    if not siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")

    session.delete(siswa)
    session.commit()
    return siswa
