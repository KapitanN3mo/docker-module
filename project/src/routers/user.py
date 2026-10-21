from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserLogin, UserLoginResponse, UserRead, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from repos.user import UserRepo
from security import Security

router = APIRouter()


@router.post("/register")
async def register_user(
    register_data: UserCreate, db: AsyncSession = Depends(get_db)
) -> UserRead:
    register_data.password_hash = Security.get_password_hash(
        register_data.password_hash
    )
    return await UserRepo(db).create(register_data)


@router.post("/login")
async def login_user(
    login_data: UserLogin, db: AsyncSession = Depends(get_db)
) -> UserLoginResponse:
    user = await UserRepo(db).get_user_by_name(login_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not Security.verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = Security.create_access_token({"user_id": user.id})
    return UserLoginResponse(
        user_id=user.id, username=user.username, access_token=token, token_type=""
    )
