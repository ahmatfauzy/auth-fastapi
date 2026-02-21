from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.session import engine
from database.base import Base
from routes.auth import router as auth_router
from routes.users import router as users_router
import models.user  

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="Async FastAPI Authentication API",
    description="Secure, Clean, Expert Authentication with PostgreSQL and FastAPI",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")

@app.get("/", tags=["health"])
async def root():
    return {"message": "Welcome to the FastAPI Clean Auth API", "status": "running"}