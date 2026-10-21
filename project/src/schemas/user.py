from pydantic import EmailStr, BaseModel, Field
from datetime import datetime


class BaseUser(BaseModel):
    username: str = Field(max_length=64)
    email: EmailStr


class UserCreate(BaseUser):
    password_hash: str = Field(validation_alias="password")


class UserRead(BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime


class UserLogin(BaseModel):
    # email: EmailStr
    username: str
    password: str


class UserLoginResponse(BaseModel):
    user_id: int
    username: str
    access_token: str
    token_type: str


# class UserRegisterRequest(BaseUser):
#     password: str