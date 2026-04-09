from datetime import datetime

from app.features.reminders.repository import ReminderRepository

class ReminderService:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    async def create_reminder(self, text: str, remind_at: datetime):
        return await self.repository.create_reminder(text, remind_at)

    async def get_all_reminders(self):
        return await self.repository.get_all_reminders()