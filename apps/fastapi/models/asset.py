from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Asset(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.id", ondelete="CASCADE"), index=True)
    file_key: Mapped[str] = mapped_column(String(512), nullable=False)
    original_name: Mapped[str] = mapped_column(String(255), nullable=False)
    size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    mime_type: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
