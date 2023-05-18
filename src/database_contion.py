from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker
from typing_extensions import AsyncGenerator

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

from src.quiz.models import Question  # isort:skip
from src.base import Base  # isort:skip

DATABASE_URL: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine: AsyncEngine = create_async_engine(DATABASE_URL)
async_session_marker: sessionmaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session
