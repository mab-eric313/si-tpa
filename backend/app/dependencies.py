import jwt
from fastapi import Depends, HTTPException, Request, status
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from config import SECRET_KEY
from app.database import get_session
from app.models import User
from config import ALGORITHM

async def get_current_user(
    request: Request, 
    session: AsyncSession = Depends(get_session)
) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Tidak bisa mem-validasi kredensial / Sesi habis",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Silahkan login terlebih dahulu"
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = await session.get(User, int(user_id))
    if not user:
        raise credentials_exception

    return user


class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Anda tidak memiliki hak akses untuk halaman ini"
            )

        return current_user


allow_admin = RoleChecker(["Admin"])
allow_pengajar = RoleChecker(["Admin", "Pengajar"])
allow_bendahara = RoleChecker(["Admin", "Bendahara"])

allow_all = RoleChecker(["Admin", "Pengajar", "Bendahara"])
