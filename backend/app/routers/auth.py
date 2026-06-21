from fastapi import APIRouter, Depends, HTTPException, Response
from pwdlib import PasswordHash
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas import UserLogin, UserResponse, UserCreate, UserUpdate
from app.database import get_session

router = APIRouter(prefix="/auth")

password_hash = PasswordHash.recommended()

# Register and Login
@router.post("/register/", response_model=UserResponse)
async def register(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    query = select(User).where(User.username == payload.username)
    existing_user = await session.scalar(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Akun sudah terdaftar")

    model_dump = payload.model_dump()
    model_dump["password"] = password_hash.hash(model_dump["password"])

    new_user = User(**model_dump)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.post("/login/", response_model=UserResponse)
async def login(
    payload: UserLogin, 
    response: Response, 
    session: AsyncSession = Depends(get_session)
):
    query = select(User).where(and_(User.username == payload.username))
    user = await session.scalar(query)
    if user and password_hash.verify(payload.password, user.password):
        response.set_cookie(
            key="user_session",
            value=str(user.id),
            httponly=True,
            samesite="lax",
            secure=False,
            max_age=1800    # Expired in 30 minutes
        )
        return user

    raise HTTPException(status_code=400, detail="Username atau Password salah")

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="user_session")
    return {"detail": "Logout successfully"}

# CRUD
@router.get("/", response_model=list[UserResponse])
async def get_all(session: AsyncSession = Depends(get_session)) -> list[User]:
    result = await session.scalars(select(User))
    return list(result.all())

@router.get("/{id}", response_model=UserResponse)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user

@router.patch("/{id}", response_model=UserResponse)
async def modify(id: int, payload: UserUpdate, session: AsyncSession = Depends(get_session)):
    """Partially modify user"""
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    for key, val in payload.model_dump(exclude_unset=True).items():
        if key == "password" and val is not None:
            val = password_hash.hash(val)
        setattr(user, key, val)

    await session.commit()
    await session.refresh(user)
    return user

@router.delete("/{id}", response_model=UserResponse)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    await session.delete(user)
    await session.commit()
    return user
