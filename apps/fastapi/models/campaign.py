from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, Enum, ForeignKey, String, TIMESTAMP, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import CampaignStatus

class Campaign(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.id", ondelete="CASCADE"))
    template_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("emailtemplate.id", ondelete="RESTRICT"))
    created_by: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id", ondelete="SET NULL"))
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    subject_override: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[CampaignStatus] = mapped_column(Enum(CampaignStatus), default=CampaignStatus.draft, index=True)
    schedule_time: Mapped[datetime | None] = mapped_column(DateTime, index=True)
    timezone: Mapped[str | None] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    template: Mapped["EmailTemplate"] = relationship(back_populates="campaigns")
    recipients: Mapped[List["CampaignRecipient"]] = relationship(back_populates="campaign", cascade="all, delete-orphan")
