from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    remind_at = Column(DateTime(timezone=True), nullable=False)