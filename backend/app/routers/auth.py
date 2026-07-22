from datetime import datetime, timedelta, timezone

import jwt
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas import UserLogin, UserResponse, UserCreate, UserUpdate
from app.database import get_session
from app.dependencies import allow_admin
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRES_MINUTE
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/auth", tags=["Authentication"])

dependencies = [Depends(allow_admin)]

password_hash = PasswordHash.recommended()

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Register and Login
@router.post("/register/", response_model=UserResponse)
async def register(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    query_register = select(User).where(User.username == payload.username)
    existing_user = await session.scalar(query_register)
    if existing_user:
        raise HTTPException(status_code=400, detail="Akun sudah terdaftar")

    model_dump = payload.model_dump()
    model_dump["password"] = password_hash.hash(model_dump["password"])

    new_user = User(**model_dump)
    session.add(new_user)
    await session.commit()

    query = select(User) \
        .options(selectinload(User.biodata)) \
        .where(User.id == new_user.id)
    result = await session.scalars(query)
    return result.first()

@router.post("/login/", response_model=UserResponse)
async def login(
    payload: UserLogin, 
    response: Response, 
    session: AsyncSession = Depends(get_session)
):
    query_login = (
        select(User)
        .options(selectinload(User.biodata))
        .where(User.username == payload.username)
    )
    user_login = await session.scalar(query_login)
    if user_login and password_hash.verify(payload.password, user_login.password):
        token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTE)
        token = create_access_token(
            data={"sub": str(user_login.id), "role": user_login.role}, 
            expires_delta=token_expires
        )
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            samesite="none",
            secure=True,
            max_age=ACCESS_TOKEN_EXPIRES_MINUTE * 60
        )

        # query = select(User) \
        #     .options(selectinload(User.biodata)) \
        #     .where(User.id == id)
        # result = await session.scalars(query)
        # user = result.first()
        # if not user:
        #     raise HTTPException(status_code=404, detail="User tidak ditemukan")
        # return user
        return user_login

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Username atau Password salah"
    )

@router.post("/logout/")
async def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/",
        httponly=True,
        samesite="lax",
        secure=False
    )
    return {"detail": "Logout successfully"}

# CRUD
@router.get("/", response_model=list[UserResponse], dependencies=dependencies)
async def get_all(session: AsyncSession = Depends(get_session)) -> list[User]:
    query = select(User) \
        .options(selectinload(User.biodata))
    result = await session.scalars(query)

    return list(result.all())

@router.get("/{id}", response_model=UserResponse, dependencies=dependencies)
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    query = select(User) \
        .options(selectinload(User.biodata)) \
        .where(User.id == id)
    result = await session.scalars(query)
    user = result.first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user

@router.patch("/{id}", response_model=UserResponse, dependencies=dependencies)
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

    query = select(User) \
        .options(selectinload(User.biodata)) \
        .where(User.id == id)
    result = await session.scalars(query)
    return result.first()

@router.delete("/{id}", response_model=UserResponse, dependencies=dependencies)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    query = select(User) \
        .options(selectinload(User.biodata)) \
        .where(User.id == id)
    result = await session.scalars(query)
    user = result.first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    await session.delete(user)
    await session.commit()
    return user
