from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.models import User

class RoleChecker:
    def __init__(self, allowed_rules: list[str]):
        self.allowed_rules = allowed_rules

    async def __call__(
        self, user_id: int, session: AsyncSession = Depends(get_session)
    ):
        user = await session.get(User, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="User tidak terautentikasi"
            )

        if user.role not in self.allowed_rules:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Anda tidak memiliki hak akses untuk halaman ini"
            )

        return user

async def get_current_user(
        request: Request, session, AsyncSession = Depends(get_session)
    ) -> User:
    user_id = request.cookies.get("user_session")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Silahkan login terlebih dahulu"
        )

    user = await session.get(User, int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Sesi tidak valid, user tidak ditemukan"
        )
    return user

allow_admin = ["admin"]
allow_pengajar = ["admin, pengajar"]
allow_bendahara = ["admin, bendahara"]
