from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy import BigInteger, Enum, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import SubscriberStatus

class Subscriber(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(BigInteger, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(64))
    last_name: Mapped[str | None] = mapped_column(String(64))
    status: Mapped[SubscriberStatus] = mapped_column(
        Enum(SubscriberStatus), default=SubscriberStatus.active
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    lists: Mapped[List["ListSubscriber"]] = relationship(back_populates="subscriber", cascade="all, delete-orphan")
