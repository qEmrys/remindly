from fastapi import APIRouter
from app.api.health import router as health_router
from app.features.reminders.router import router as reminders_router

api_router = APIRouter(prefix="/api")

api_router.include_router(health_router, tags=["health"])
api_router.include_router(reminders_router, prefix="/reminders", tags=["reminders"])
