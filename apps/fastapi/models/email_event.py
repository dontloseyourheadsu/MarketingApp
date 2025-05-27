from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, Enum, ForeignKey, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import EmailEventType

class EmailEvent(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    campaign_recipient_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("campaignrecipient.id", ondelete="CASCADE"))
    event_type: Mapped[EmailEventType] = mapped_column(Enum(EmailEventType))
    event_ts: Mapped[datetime] = mapped_column(DateTime, index=True)
    meta_json: Mapped[dict | None] = mapped_column(JSON)

    campaign_recipient: Mapped["CampaignRecipient"] = relationship(back_populates="email_events")
