from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
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

@router.post("/", response_model=UserResponse)
async def create(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    """Create user"""
    user = User(**payload.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
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
        raise HTTPException(status_code=400, detail="Account has already been registered")

    new_user = User(**payload.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.post("/login/", response_model=UserLogin)
async def login(payload: UserLogin, session: AsyncSession = Depends(get_session)):
    query_get_username = select(User).where(User.username == payload.username)
    query_get_password = select(User).where(User.password == payload.password)

    existing_username = await session.scalar(query_get_username)
    existing_password = await session.scalar(query_get_password)
    if existing_username and existing_password:
        return payload
    else:
        return HTTPException(status_code=400, detail="Incorrect username or password")
