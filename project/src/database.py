from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from dotenv import load_dotenv
from os import getenv

load_dotenv()

engine = create_async_engine(str(getenv("DATABASE_URL")), pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()