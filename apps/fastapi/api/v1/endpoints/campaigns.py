from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ....core.database import get_db
from ....schemas.campaign import CampaignCreate, CampaignRead, CampaignUpdate
from ....services.campaign_service import (
    create_campaign,
    get_campaign,
    list_campaigns,
    update_campaign,
    delete_campaign,
)

router = APIRouter()

@router.post("/", response_model=CampaignRead, status_code=status.HTTP_201_CREATED)
def create(campaign_in: CampaignCreate, db: Session = Depends(get_db)):
    return create_campaign(db, campaign_in)

@router.get("/", response_model=List[CampaignRead])
def list_(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return list_campaigns(db, skip, limit)

@router.get("/{campaign_id}", response_model=CampaignRead)
def read(campaign_id: int, db: Session = Depends(get_db)):
    campaign = get_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.put("/{campaign_id}", response_model=CampaignRead)
def update(
    campaign_id: int,
    campaign_in: CampaignUpdate,
    db: Session = Depends(get_db),
):
    return update_campaign(db, campaign_id, campaign_in)

@router.delete("/{campaign_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(campaign_id: int, db: Session = Depends(get_db)):
    delete_campaign(db, campaign_id)