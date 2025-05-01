from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.incident import SeverityLevel

class IncidentBase(BaseModel):
    title: str
    description: str
    severity: SeverityLevel

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id: int
    reported_at: datetime

    class Config:
        from_attributes = True 