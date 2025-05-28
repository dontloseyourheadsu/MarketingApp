from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ....core.database import get_db
from ....schemas.subscriber import SubscriberCreate, SubscriberRead, SubscriberUpdate
from ....services.subscriber_service import (
    create_subscriber,
    delete_subscriber,
    get_subscriber,
    list_subscribers,
    update_subscriber,
)

router = APIRouter()

@router.post("/", response_model=SubscriberRead, status_code=status.HTTP_201_CREATED)
def create(
    subscriber_in: SubscriberCreate,
    db: Session = Depends(get_db),
):
    return create_subscriber(db, subscriber_in)

@router.get("/", response_model=List[SubscriberRead])
def list_(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return list_subscribers(db, skip, limit)

@router.get("/{subscriber_id}", response_model=SubscriberRead)
def read(subscriber_id: int, db: Session = Depends(get_db)):
    subscriber = get_subscriber(db, subscriber_id)
    if not subscriber:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    return subscriber

@router.put("/{subscriber_id}", response_model=SubscriberRead)
def update(
    subscriber_id: int,
    subscriber_in: SubscriberUpdate,
    db: Session = Depends(get_db),
):
    return update_subscriber(db, subscriber_id, subscriber_in)

@router.delete("/{subscriber_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(subscriber_id: int, db: Session = Depends(get_db)):
    delete_subscriber(db, subscriber_id)