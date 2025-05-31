from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from ..models.refresh_token import RefreshToken


def save_refresh_token(db: Session, payload: dict) -> RefreshToken:
    token = RefreshToken(
        jti=payload["jti"],
        user_id=int(payload["sub"]),
        expires_at=datetime.fromtimestamp(payload["exp"]),
    )
    db.add(token)
    db.commit()
    return token


def revoke_token(db: Session, jti: str) -> None:
    token = db.query(RefreshToken).filter(RefreshToken.jti == jti).first()
    if token and not token.revoked:
        token.revoked = True
        db.commit()


def is_token_revoked(db: Session, jti: str) -> bool:
    token: Optional[RefreshToken] = db.query(RefreshToken).filter(RefreshToken.jti == jti).first()
    return token is None or token.revoked or token.expires_at <= datetime.utcnow()