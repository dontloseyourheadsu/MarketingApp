from enum import Enum

class UserRole(str, Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class SubscriberStatus(str, Enum):
    active = "active"
    unsubscribed = "unsubscribed"
    bounced = "bounced"
    complained = "complained"

class CampaignStatus(str, Enum):
    draft = "draft"
    scheduled = "scheduled"
    sending = "paused"  # sending + paused
    completed = "completed"
    canceled = "canceled"

class RecipientStatus(str, Enum):
    pending = "pending"
    sent = "sent"
    delivered = "delivered"
    bounced = "bounced"
    opened = "opened"
    clicked = "clicked"
    complained = "complained"
    unsubscribed = "unsubscribed"

class EmailEventType(str, Enum):
    delivered = "delivered"
    open = "open"
    click = "click"
    bounce = "bounce"
    complaint = "complaint"
    unsubscribe = "unsubscribe"