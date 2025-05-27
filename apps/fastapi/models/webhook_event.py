from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, String, Enum, Integer, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class WebhookEvent(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    webhook_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("webhook.id", ondelete="CASCADE"))
    event_type: Mapped[str] = mapped_column(String(64))
    payload_json: Mapped[dict] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(Enum("pending", "success", "failed", name="webhook_status"), default="pending")
    attempts: Mapped[int] = mapped_column(Integer, default=0)
    last_attempt_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    webhook: Mapped["Webhook"] = relationship(back_populates="deliveries")
