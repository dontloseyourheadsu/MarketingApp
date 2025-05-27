from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, Enum, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import RecipientStatus

class CampaignRecipient(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    campaign_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("campaign.id", ondelete="CASCADE"))
    subscriber_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriber.id", ondelete="CASCADE"))
    list_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("lists.id", ondelete="SET NULL"))
    sent_at: Mapped[datetime | None] = mapped_column(DateTime)
    status: Mapped[RecipientStatus] = mapped_column(Enum(RecipientStatus), default=RecipientStatus.pending, index=True)
    open_count: Mapped[int] = mapped_column(default=0)
    click_count: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    campaign: Mapped["Campaign"] = relationship(back_populates="recipients")
    email_events: Mapped[List["EmailEvent"]] = relationship(back_populates="campaign_recipient", cascade="all, delete-orphan")
