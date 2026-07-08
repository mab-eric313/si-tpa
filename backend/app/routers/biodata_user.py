from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import BiodataUser
from app.schemas import BiodataUserResponse, BiodataUserCreate, BiodataUserUpdate
from app.database import get_session
from app.dependencies import allow_admin, allow_bendahara

router = APIRouter(prefix="/biodata-user")

read_dependencies = [Depends(allow_bendahara)]
write_dependencies = [Depends(allow_admin)]

@router.get("/", response_model=list[BiodataUserResponse], dependencies=read_dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[BiodataUser]:
    result = await session.scalars(select(BiodataUser))
    return list(result.all())

@router.get("/{id}", response_model=BiodataUserResponse, dependencies=read_dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")
    return kelas

@router.post("/", response_model=BiodataUserResponse, dependencies=write_dependencies)
async def create(payload: BiodataUserCreate, session: AsyncSession = Depends(get_session)):
    """Create kelas"""
    kelas = BiodataUser(**payload.model_dump())
    session.add(kelas)
    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/{id}", response_model=BiodataUserResponse, dependencies=write_dependencies)
async def modify(id: int, payload: BiodataUserUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify kelas"""
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(kelas, key, val)

    await session.commit()
    await session.refresh(kelas)
    return kelas

@router.patch("/by-user/{user_id}", response_model=BiodataUserResponse, dependencies=write_dependencies)
async def modify_by_user_id(
    user_id: int, payload: BiodataUserUpdate, session: AsyncSession = Depends(get_session)
):
    result = await session.scalars(
        select(BiodataUser).where(BiodataUser.user_id == user_id)
    )
    biodata = result.first()
    if not biodata:
        biodata = BiodataUser(user_id=user_id, **payload.model_dump(exclude_unset=True))
        session.add(biodata)
    else:
        for key, val in payload.model_dump(exclude_unset=True).items():
            setattr(biodata, key, val)

    await session.commit()
    await session.refresh(biodata)
    return biodata

@router.delete("/by-user/{user_id}", response_model=BiodataUserResponse, dependencies=write_dependencies)
async def delete_by_user_id(
    user_id: int, session: AsyncSession = Depends(get_session)
):
    result = await session.scalars(
        select(BiodataUser).where(BiodataUser.user_id == user_id)
    )
    biodata = result.first()
    if not biodata:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")

    await session.delete(biodata)
    await session.commit()
    return biodata

@router.delete("/{id}", response_model=BiodataUserResponse, dependencies=write_dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    kelas = await session.get(BiodataUser, id)
    if not kelas:
        raise HTTPException(status_code=404, detail="BiodataUser tidak ditemukan")

    await session.delete(kelas)
    await session.commit()
    return kelas

