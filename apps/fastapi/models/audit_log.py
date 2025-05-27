from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, String, JSON, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class AuditLog(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.id", ondelete="CASCADE"))
    user_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("user.id", ondelete="SET NULL"))
    action: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    context_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
