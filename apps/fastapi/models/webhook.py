from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, ForeignKey, String, TIMESTAMP, Enum, JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import EmailEventType

class Webhook(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.id", ondelete="CASCADE"))
    target_url: Mapped[str] = mapped_column(String(512), nullable=False)
    event_types: Mapped[set[EmailEventType]] = mapped_column(
        Enum(EmailEventType, native_enum=False)
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    deliveries: Mapped[List["WebhookEvent"]] = relationship(back_populates="webhook", cascade="all, delete-orphan")
