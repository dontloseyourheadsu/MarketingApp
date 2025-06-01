from typing import List, Optional
from sqlalchemy.orm import Session
from ..tasks.email import send_campaign_email
from ..models.campaign_recipient import CampaignRecipient
from ..models.campaign import Campaign
from ..schemas.campaign import CampaignCreate, CampaignUpdate

def list_campaigns(db: Session, skip: int = 0, limit: int = 100) -> List[Campaign]:
    return db.query(Campaign).offset(skip).limit(limit).all()

def get_campaign(db: Session, campaign_id: int) -> Optional[Campaign]:
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()

def create_campaign(db: Session, data: CampaignCreate) -> Campaign:
    campaign = Campaign(**data.model_dump())
    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return campaign

def update_campaign(db: Session, campaign_id: int, data: CampaignUpdate) -> Campaign:
    campaign = get_campaign(db, campaign_id)
    if not campaign:
        raise ValueError("Campaign not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(campaign, field, value)
    db.commit()
    db.refresh(campaign)
    return campaign

def delete_campaign(db: Session, campaign_id: int) -> None:
    campaign = get_campaign(db, campaign_id)
    if campaign:
        db.delete(campaign)
        db.commit()

def dispatch_campaign(db: Session, campaign_id: int):
    """
    Enqueue all recipients of a campaign.
    Owner/admin only.
    """
    recipients = (
        db.query(CampaignRecipient.id)
        .filter(CampaignRecipient.campaign_id == campaign_id, CampaignRecipient.status == "pending")
        .all()
    )
    for (recipient_id,) in recipients:
        send_campaign_email.delay(recipient_id)