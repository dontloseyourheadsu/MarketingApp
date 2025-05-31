from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, Query

from ....core.database import get_db
from ....core.deps import (
    require_roles,
    pagination_params,
    paginate,
    add_pagination_headers,
)
from ....schemas.campaign import CampaignCreate, CampaignRead, CampaignUpdate
from ....services.campaign_service import (
    create_campaign,
    delete_campaign,
    get_campaign,
    update_campaign,
)
from ....models.campaign import Campaign

router = APIRouter()

@router.get("/", response_model=List[CampaignRead])
def list_(
    _: Annotated[None, Depends(require_roles("owner", "admin", "member"))],
    pag: Annotated[dict, Depends(pagination_params)],
    db: Session = Depends(get_db),
):
    query: Query = db.query(Campaign)
    total, items = paginate(query, **pag)
    response = JSONResponse(content=[CampaignRead.model_validate(i) for i in items])
    add_pagination_headers(response, total, pag["skip"], pag["limit"])
    return response

@router.post(
    "/", response_model=CampaignRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles("owner", "admin"))],
)
def create(campaign_in: CampaignCreate, db: Session = Depends(get_db)):
    return create_campaign(db, campaign_in)

@router.get(
    "/{campaign_id}", response_model=CampaignRead,
    dependencies=[Depends(require_roles("owner", "admin", "member"))],
)
def read(campaign_id: int, db: Session = Depends(get_db)):
    campaign = get_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.put(
    "/{campaign_id}", response_model=CampaignRead,
    dependencies=[Depends(require_roles("owner", "admin"))],
)
def update(campaign_id: int, data: CampaignUpdate, db: Session = Depends(get_db)):
    return update_campaign(db, campaign_id, data)

@router.delete(
    "/{campaign_id}", status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_roles("owner"))],
)
def delete(campaign_id: int, db: Session = Depends(get_db)):
    delete_campaign(db, campaign_id)
