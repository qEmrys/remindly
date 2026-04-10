from datetime import datetime

from app.features.reminders.repository import ReminderRepository

class ReminderService:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    async def create_reminder(self, text: str, remind_at: datetime):
        return await self.repository.create_reminder(text, remind_at)

    async def get_all_reminders(self):
        return await self.repository.get_all_reminders()
    
    async def get_reminder_by_id(self, reminder_id: int):
        return await self.repository.get_reminder_by_id(reminder_id)

    async def delete_reminder(self, reminder_id: int):
        return await self.repository.delete_reminder(reminder_id)

    async def update_reminder(self, reminder_id: int, text: str | None = None, remind_at: datetime | None = None):
        return await self.repository.update_reminder(reminder_id, text, remind_at)