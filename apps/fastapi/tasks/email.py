import aioboto3
import asyncio
from datetime import datetime

from ..models.campaign_recipient import CampaignRecipient
from ..core.config import settings
from . import celery

SES_CHARSET = "UTF-8"

@celery.task(name="send_campaign_email")
def send_campaign_email(recipient_id: int):
    """
    Synchronous Celery task (still non-blocking for FastAPI).  
    It spins up an event loop just for SES call via aioboto3.
    """
    asyncio.run(_async_send(recipient_id))

async def _async_send(recipient_id: int):
    import sqlalchemy as sa
    from sqlalchemy.orm import Session
    from ..core.database import SessionLocal
    from ..models.email_template import EmailTemplate
    from ..models.subscriber import Subscriber

    db: Session = SessionLocal()

    rec: CampaignRecipient = db.get(CampaignRecipient, recipient_id)
    if not rec:
        return

    tmpl: EmailTemplate = db.get(EmailTemplate, rec.campaign.template_id)
    sub: Subscriber = db.get(Subscriber, rec.subscriber_id)

    html_body = tmpl.html_body.replace("{{first_name}}", sub.first_name or "")
    text_body = tmpl.text_body.replace("{{first_name}}", sub.first_name or "") if tmpl.text_body else None

    async with aioboto3.client("ses", region_name=settings.AWS_REGION) as ses:
        await ses.send_email(
            Source="no-reply@yourdomain.com",
            Destination={"ToAddresses": [sub.email]},
            Message={
                "Subject": {"Data": tmpl.subject, "Charset": SES_CHARSET},
                "Body": {
                    "Html": {"Data": html_body, "Charset": SES_CHARSET},
                    **(
                        {"Text": {"Data": text_body, "Charset": SES_CHARSET}}
                        if text_body
                        else {}
                    ),
                },
            },
        )
    # Update status
    rec.sent_at = datetime.utcnow()
    rec.status = "sent"
    db.commit()
    db.close()