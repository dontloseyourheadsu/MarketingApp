from datetime import datetime
from pydantic import BaseModel, Field

class ORMBase(BaseModel):
    id: int = Field(..., example=1)
    created_at: datetime

    class Config:
        from_attributes = True