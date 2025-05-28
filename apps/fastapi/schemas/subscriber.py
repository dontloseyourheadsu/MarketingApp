from typing import Optional
from pydantic import EmailStr, Field

from .generic import ORMBase

class SubscriberBase(ORMBase):
    email: EmailStr
    first_name: Optional[str] = Field(None, max_length=64)
    last_name: Optional[str] = Field(None, max_length=64)

class SubscriberCreate(SubscriberBase):
    pass

class SubscriberUpdate(SubscriberBase):
    email: Optional[EmailStr] = None

class SubscriberRead(SubscriberBase):
    pass