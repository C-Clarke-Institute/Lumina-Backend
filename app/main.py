from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import AsyncSessionLocal

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