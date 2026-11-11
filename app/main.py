from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.db.session import engine
from app.core.config import settings
from sqlmodel import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables if they don't exist
    print("Requesting database connection...")
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))  # Simple query to test the connection
        print("Database connection successful.")
        await conn.run_sync(lambda conn: conn.execute(text("SELECT 1")))  # Test sync execution
        print("Database sync execution successful.")
       
           
    print(f"Successfully connected {settings.Backend_URL} to the database {settings.DATABASE_URL}")

    yield


app = FastAPI(title="CSC 301 Final Project API", version="1.0.0", license_info={}, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Allow all origins for simplicity; adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

