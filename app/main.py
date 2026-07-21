from fastapi import FastAPI

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