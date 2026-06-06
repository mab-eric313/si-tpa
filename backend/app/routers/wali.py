from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Wali
from app.schemas import WaliResponse, WaliCreate, WaliUpdate
from app.database import get_session

router = APIRouter(prefix="/wali")

@router.get("/", response_model=list[WaliResponse])
def get_all(session: Session = Depends(get_session)) -> list[Wali]:
    return list(session.scalars(select(Wali)).all())

@router.get("/{id}", response_model=WaliResponse)
def get_one(id: int, session: Session = Depends(get_session)):
    wali = session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")
    return wali

@router.post("/", response_model=WaliResponse)
def create(payload: WaliCreate, session: Session = Depends(get_session)):
    """Create wali"""
    wali = Wali(**payload.model_dump())
    session.add(wali)
    session.commit()
    session.refresh(wali)
    return wali

@router.patch("/{id}", response_model=WaliResponse)
def modify(id: int, payload: WaliUpdate, session: Session = Depends(get_session)):
    """Partially modify wali"""
    wali = session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(wali, key, val)

    session.commit()
    session.refresh(wali)
    return wali

@router.delete("/{id}", response_model=WaliResponse)
def delete(id: int, session: Session = Depends(get_session)):
    wali = session.get(Wali, id)
    if not wali:
        raise HTTPException(status_code=404, detail="Wali tidak ditemukan")

    session.delete(wali)
    session.commit()
    return wali


