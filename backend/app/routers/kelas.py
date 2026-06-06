from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Kelas
from app.schemas import KelasResponse, KelasCreate, KelasUpdate
from app.database import get_session

router = APIRouter(prefix="/kelas")

@router.get("/", response_model=list[KelasResponse])
def get_all(session: Session = Depends(get_session)) -> list[Kelas]:
    return list(session.scalars(select(Kelas)).all())

@router.get("/{id}", response_model=KelasResponse)
def get_one(id: int, session: Session = Depends(get_session)):
    kelas = session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")
    return kelas

@router.post("/", response_model=KelasResponse)
def create(payload: KelasCreate, session: Session = Depends(get_session)):
    """Create kelas"""
    kelas = Kelas(**payload.model_dump())
    session.add(kelas)
    session.commit()
    session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=KelasResponse)
def modify(id: int, payload: KelasUpdate, session: Session = Depends(get_session)):
    """Partially modify kelas"""
    kelas = session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    session.commit()
    session.refresh(kelas)
    return kelas

@router.delete("/{id}", response_model=KelasResponse)
def delete(id: int, session: Session = Depends(get_session)):
    kelas = session.get(Kelas, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")

    session.delete(kelas)
    session.commit()
    return kelas

