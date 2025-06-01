from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, Query
from ....core.rate_limit import limit
from ....core.database import get_db
from ....core.deps import (
    require_roles,
    pagination_params,
    paginate,
    add_pagination_headers,
)
from ....schemas.subscriber import SubscriberCreate, SubscriberRead, SubscriberUpdate
from ....services.subscriber_service import (
    create_subscriber,
    delete_subscriber,
    get_subscriber,
    update_subscriber,
)
from ....models.subscriber import Subscriber

router = APIRouter()

# --- List ------------------------------------------------------------------- #
@router.get("/", response_model=List[SubscriberRead],dependencies=[Depends(limit())])
def list_(
    _: Annotated[None, Depends(require_roles("owner", "admin", "member"))],
    pag: Annotated[dict, Depends(pagination_params)],
    db: Session = Depends(get_db),
):
    query: Query = db.query(Subscriber)
    total, items = paginate(query, **pag)
    response = JSONResponse(content=[SubscriberRead.model_validate(i) for i in items])
    add_pagination_headers(response, total, pag["skip"], pag["limit"])
    return response


# --- CRUD ------------------------------------------------------------------- #
@router.post(
    "/", response_model=SubscriberRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles("owner", "admin")), Depends(limit())],
)
def create(subscriber_in: SubscriberCreate, db: Session = Depends(get_db)):
    return create_subscriber(db, subscriber_in)

@router.get(
    "/{subscriber_id}", response_model=SubscriberRead,
    dependencies=[Depends(require_roles("owner", "admin", "member")), Depends(limit())],
)
def read(subscriber_id: int, db: Session = Depends(get_db)):
    subscriber = get_subscriber(db, subscriber_id)
    if not subscriber:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    return subscriber

@router.put(
    "/{subscriber_id}", response_model=SubscriberRead,
    dependencies=[Depends(require_roles("owner", "admin")), Depends(limit())],
)
def update(subscriber_id: int, data: SubscriberUpdate, db: Session = Depends(get_db)):
    return update_subscriber(db, subscriber_id, data)

@router.delete(
    "/{subscriber_id}", status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_roles("owner")), Depends(limit())],
)
def delete(subscriber_id: int, db: Session = Depends(get_db)):
    delete_subscriber(db, subscriber_id)