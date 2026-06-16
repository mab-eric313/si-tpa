from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.schemas import UserLogin, UserResponse, UserCreate, UserUpdate
from app.database import get_session

router = APIRouter(prefix="/auth")

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

# Register and Login
@router.post("/register/", response_model=UserResponse)
async def register(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    query = select(User).where(User.username == payload.username)
    existing_user = await session.scalar(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Akun sudah terdaftar")

    new_user = User(**payload.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.post("/login/", response_model=UserResponse)
async def login(payload: UserLogin, session: AsyncSession = Depends(get_session)):
    query = select(User).where(
        and_(
            User.username == payload.username,
            User.password == payload.password
        )
    )

    existing_user = await session.scalar(query)
    if existing_user:
        return existing_user
    else:
        raise HTTPException(status_code=400, detail="Username atau Password salah")
