from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import AsyncSessionLocal, create_tables
from app.modules.category.routers import router as category_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_tables()
    yield

app = FastAPI(title="Lumina E-Commerce API",
              version="1.0.0")



@app.get("/")
async def root():
    return {"message" : "Lumina API Running Successfully"}

@app.get("/health")
async def health():
    return {
        "status": "UP"
    }

@app.get("/db-test")
async def db_test():

    async with AsyncSessionLocal() as session:
        result = await session.execute(text("Select 1"))

        return {
            "database" : result.scalars()
        }
app.include_router(category_router)