from __future__ import annotations
from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, PrimaryKeyConstraint, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class ListSubscriber(Base):
    __tablename__ = "list_subscribers"
    __table_args__ = (
        PrimaryKeyConstraint("list_id", "subscriber_id"),
    )

    list_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("lists.id", ondelete="CASCADE"))
    subscriber_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriber.id", ondelete="CASCADE"))
    added_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    list_: Mapped["List"] = relationship(back_populates="subscribers")
    subscriber: Mapped["Subscriber"] = relationship(back_populates="lists")
