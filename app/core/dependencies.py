from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from fastapi import Depends
from app.features.reminders.repository import ReminderRepository
from app.features.reminders.service import ReminderService
from app.core.database import SessionLocal



async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

def get_reminder_repository(db: AsyncSession = Depends(get_db)) -> ReminderRepository:
    return ReminderRepository(db)

def get_reminder_service(repository: ReminderRepository = Depends(get_reminder_repository)) -> ReminderService:
    return ReminderService(repository)