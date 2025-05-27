# apps/fastapi_app/models/email_template.py
from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class EmailTemplate(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.id", ondelete="CASCADE"))
    created_by: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id", ondelete="SET NULL"))
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    html_body: Mapped[str] = mapped_column(Text, nullable=False)
    text_body: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    campaigns: Mapped[List["Campaign"]] = relationship(back_populates="template")
