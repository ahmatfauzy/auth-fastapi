from fastapi import APIRouter, Depends
from models.user import User
from schemas.user import UserResponse
from routes.dependencies import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
