from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ReminderCreate(BaseModel):
    text: str
    remind_at: datetime

class ReminderOut(ReminderCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ReminderUpdate(BaseModel):
    text: str | None = None
    remind_at: datetime | None = None