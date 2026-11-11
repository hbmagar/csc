from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "healthy"}

@api_router.get("/hi", tags=["Greeting"])
async def say_hi():
    """
    A simple endpoint to greet the user.
    """
    return {"message": "Hello, welcome to the API!"}