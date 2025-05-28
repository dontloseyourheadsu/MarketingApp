from datetime import datetime
from typing import Optional

from pydantic import Field

from .generic import ORMBase

class CampaignBase(ORMBase):
    name: str = Field(..., max_length=128)
    template_id: int
    status: str
    schedule_time: Optional[datetime] = None

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(CampaignBase):
    name: Optional[str] = None
    template_id: Optional[int] = None
    status: Optional[str] = None

class CampaignRead(CampaignBase):
    pass