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