from schemas.user import UserCreate
from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional


class UserRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_data: UserCreate) -> User:
        user = User(**user_data.model_dump())
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_by_id(self, _id: int) -> Optional[User]:
        statement = select(User).where(User.id == _id)
        res = await self.db.execute(statement)
        return res.scalar_one_or_none()

    async def get_user_by_name(self, name: str) -> Optional[User]:
        statement = select(User).where(User.username == name)
        res = await self.db.execute(statement)
        return res.scalar_one_or_none()
