from fastapi import APIRouter, Depends
from app.features.reminders.service import ReminderService
from app.features.reminders.schemas import ReminderCreate, ReminderOut
from app.core.dependencies import get_reminder_service
from typing import List

router = APIRouter()

@router.post("/", response_model=ReminderOut)
async def create_reminder(data: ReminderCreate, service: ReminderService = Depends(get_reminder_service)):
    return await service.create_reminder(data.text, data.remind_at)

@router.get("/", response_model=List[ReminderOut])
async def get_reminders(service: ReminderService = Depends(get_reminder_service)):
    return await service.get_all_reminders()