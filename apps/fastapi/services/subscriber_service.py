from typing import List, Optional
from sqlalchemy.orm import Session

from ..models.subscriber import Subscriber
from ..schemas.subscriber import SubscriberCreate, SubscriberUpdate

def list_subscribers(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(Subscriber)
    return query.offset(skip).limit(limit).all()

def get_subscriber(db: Session, subscriber_id: int) -> Optional[Subscriber]:
    return db.query(Subscriber).filter(Subscriber.id == subscriber_id).first()

def create_subscriber(db: Session, data: SubscriberCreate) -> Subscriber:
    subscriber = Subscriber(**data.model_dump())
    db.add(subscriber)
    db.commit()
    db.refresh(subscriber)
    return subscriber

def update_subscriber(db: Session, subscriber_id: int, data: SubscriberUpdate) -> Subscriber:
    subscriber = get_subscriber(db, subscriber_id)
    if not subscriber:
        raise ValueError("Subscriber not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(subscriber, field, value)
    db.commit()
    db.refresh(subscriber)
    return subscriber

def delete_subscriber(db: Session, subscriber_id: int) -> None:
    subscriber = get_subscriber(db, subscriber_id)
    if subscriber:
        db.delete(subscriber)
        db.commit()