from fastapi import Depends, APIRouter

from app.dependencies import RoleChecker, allow_admin, allow_bendahara, allow_pengajar
from app.models import User
from app.schemas import UserResponse

router = APIRouter()

# Admin
@router.get("/admin", response_model=UserResponse)
async def admin_dashboard(
    current_user: User = Depends(RoleChecker(allow_admin))
):
    return current_user


# Bendahara
@router.get("/bendahara", response_model=UserResponse)
async def bendahara_dashboard(
    current_user: User = Depends(RoleChecker(allow_bendahara))
):
    return current_user


# Bendahara
@router.get("/pengajar", response_model=UserResponse)
async def pengajar_dashboard(
    current_user: User = Depends(RoleChecker(allow_pengajar))
):
    return current_user
