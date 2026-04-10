from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.features.reminders.models import Reminder


class ReminderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_reminder(self, text: str, remind_at: datetime) -> Reminder:
        new_reminder = Reminder(text=text, remind_at=remind_at)
        self.db.add(new_reminder)
        await self.db.commit()
        await self.db.refresh(new_reminder)
        return new_reminder

    async def get_all_reminders(self) -> list[Reminder]:
        result = await self.db.execute(select(Reminder))
        reminders = result.scalars().all()
        return reminders
    
    async def get_reminder_by_id(self, reminder_id: int) -> Reminder | None:
        result = await self.db.execute(select(Reminder).where(Reminder.id == reminder_id))
        reminder = result.scalars().first()
        return reminder
    
    async def delete_reminder(self, reminder_id: int) -> bool:
        reminder = await self.get_reminder_by_id(reminder_id)
        if reminder:
            await self.db.delete(reminder)
            await self.db.commit()
            return True
        return False
    
    async def update_reminder(self, reminder_id: int, text: str | None = None, remind_at: datetime | None = None) -> Reminder | None:
        reminder = await self.get_reminder_by_id(reminder_id)
        if reminder:
            if text is not None:
                reminder.text = text
            if remind_at is not None:
                reminder.remind_at = remind_at
            await self.db.commit()
            await self.db.refresh(reminder)
            return reminder
        return None