from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

from faker import Faker
from passlib.hash import bcrypt
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
from apps.fastapi.models import (
    Organization,
    User,
    Subscriber,
    List,
    ListSubscriber,
    EmailTemplate,
    Campaign,
)

# --- configuration ----------------------------------------------------------
DB_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://appuser:app_password@localhost:3306/email_marketing"
)
DEFAULT_ORG_NAME = os.getenv("DEFAULT_ORG_NAME", "ExampleCorp")
DEFAULT_ADMIN_EMAIL = os.getenv("DEFAULT_ADMIN_EMAIL", "owner@example.com")
DEFAULT_ADMIN_PW = os.getenv("DEFAULT_ADMIN_PW", "ChangeMe123!")

faker = Faker()
engine = create_engine(DB_URL, pool_pre_ping=True, echo=False, future=True)


def get_or_create_organization(session: Session, name: str) -> Organization:
    org = session.scalar(select(Organization).where(Organization.name == name))
    if org:
        return org
    org = Organization(name=name)
    session.add(org)
    session.flush()
    return org


def get_or_create_admin_user(session: Session, org: Organization) -> User:
    user = session.scalar(
        select(User).where(User.organization_id == org.id, User.email == DEFAULT_ADMIN_EMAIL)
    )
    if user:
        return user
    user = User(
        organization_id=org.id,
        email=DEFAULT_ADMIN_EMAIL,
        hashed_password=bcrypt.hash(DEFAULT_ADMIN_PW),
        role="owner",
    )
    session.add(user)
    session.flush()
    return user


def seed_subscribers(session: Session, org: Organization, qty: int = 25) -> list[Subscriber]:
    existing = (
        session.execute(
            select(Subscriber.id).where(Subscriber.organization_id == org.id).limit(qty)
        )
        .scalars()
        .all()
    )
    if existing:
        # Don’t create duplicates on re-run
        return session.scalars(
            select(Subscriber).where(Subscriber.organization_id == org.id).limit(qty)
        ).all()

    subs = []
    for _ in range(qty):
        profile = faker.profile(fields=["mail", "name"])
        first, last = profile["name"].split(maxsplit=1)
        subs.append(
            Subscriber(
                organization_id=org.id,
                email=profile["mail"],
                first_name=first,
                last_name=last,
            )
        )
    session.add_all(subs)
    session.flush()
    return subs


def seed_list(session: Session, org: Organization, subs: list[Subscriber]) -> List:
    lst = session.scalar(
        select(List).where(List.organization_id == org.id, List.name == "Monthly Newsletter")
    )
    if lst:
        return lst
    lst = List(
        organization_id=org.id,
        name="Monthly Newsletter",
        description="General updates newsletter",
    )
    session.add(lst)
    session.flush()

    # pivot table rows
    session.add_all(
        ListSubscriber(list_id=lst.id, subscriber_id=s.id, added_at=datetime.now(timezone.utc))
        for s in subs
    )
    return lst


def seed_template(session: Session, org: Organization, admin: User) -> EmailTemplate:
    tmpl = session.scalar(
        select(EmailTemplate).where(
            EmailTemplate.organization_id == org.id, EmailTemplate.name == "Welcome Template"
        )
    )
    if tmpl:
        return tmpl
    tmpl = EmailTemplate(
        organization_id=org.id,
        created_by=admin.id,
        name="Welcome Template",
        subject="Welcome to ExampleCorp!",
        html_body="<h1>Hello {{first_name}}</h1><p>Thanks for joining us.</p>",
        text_body="Hello {{first_name}},\n\nThanks for joining us.",
    )
    session.add(tmpl)
    session.flush()
    return tmpl


def seed_campaign(session: Session, org: Organization, admin: User, tmpl: EmailTemplate) -> None:
    exists = session.scalar(
        select(Campaign).where(Campaign.organization_id == org.id, Campaign.name == "Welcome Campaign")
    )
    if exists:
        return
    campaign = Campaign(
        organization_id=org.id,
        template_id=tmpl.id,
        created_by=admin.id,
        name="Welcome Campaign",
        status="draft",
    )
    session.add(campaign)


def main() -> None:
    with Session(engine) as session:
        org = get_or_create_organization(session, DEFAULT_ORG_NAME)
        admin = get_or_create_admin_user(session, org)
        subs = seed_subscribers(session, org, qty=25)
        lst = seed_list(session, org, subs)
        tmpl = seed_template(session, org, admin)
        seed_campaign(session, org, admin, tmpl)

        session.commit()

    print("🌱  Database seeded successfully!")


if __name__ == "__main__":
    main()
