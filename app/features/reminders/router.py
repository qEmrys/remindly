from fastapi import APIRouter, Depends, HTTPException
from app.features.reminders.service import ReminderService
from app.features.reminders.schemas import ReminderCreate, ReminderOut, ReminderUpdate
from app.core.dependencies import get_reminder_service
from typing import List

router = APIRouter()

@router.post("/", response_model=ReminderOut)
async def create_reminder(data: ReminderCreate, service: ReminderService = Depends(get_reminder_service)):
    return await service.create_reminder(data.text, data.remind_at)

@router.get("/", response_model=List[ReminderOut])
async def get_reminders(service: ReminderService = Depends(get_reminder_service)):
    return await service.get_all_reminders()

@router.get("/{reminder_id}", response_model=ReminderOut)
async def get_reminder(reminder_id: int, service: ReminderService = Depends(get_reminder_service)):
    reminder = await service.get_reminder_by_id(reminder_id)
    if reminder is None:
        raise HTTPException(status_code=404, detail=f"Reminder with id {reminder_id} not found")
    return reminder

@router.patch("/{reminder_id}", response_model=ReminderOut)
async def update_reminder(reminder_id: int, data: ReminderUpdate, service: ReminderService = Depends(get_reminder_service)):
    updated_reminder = await service.update_reminder(reminder_id, data.text, data.remind_at)
    if data.text is None and data.remind_at is None:
        raise HTTPException(status_code=400, detail=f"At least one field (text or remind_at) must be provided for update")
    if updated_reminder is None:
        raise HTTPException(status_code=404, detail=f"Reminder with id {reminder_id} not found")
    return updated_reminder

@router.delete("/{reminder_id}", status_code=204)
async def delete_reminder(reminder_id: int, service: ReminderService = Depends(get_reminder_service)):
    success = await service.delete_reminder(reminder_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Reminder with id {reminder_id} not found")
    return success