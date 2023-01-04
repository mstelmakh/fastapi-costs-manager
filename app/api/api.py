from fastapi import APIRouter

from app.api.endpoints import operations

api_router = APIRouter()
api_router.include_router(operations.router)
