from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.base import Base
from app.core.config import settings

engine = create_async_engine(settings.database_url,
                             echo=True,
                             pool_size=settings.POOL_SIZE,
                             max_overflow=settings.MAX_OVER_FLOW)

AsyncSessionLocal =  async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

#test

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def create_tables():
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)