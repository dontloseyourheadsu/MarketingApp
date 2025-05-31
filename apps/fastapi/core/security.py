from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Union
from uuid import uuid4

from jose import JWTError, jwt
from passlib.context import CryptContext

from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


# --------------------------------------------------------------------------- #
# Password helpers                                                            #
# --------------------------------------------------------------------------- #
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# --------------------------------------------------------------------------- #
# JWT helpers                                                                 #
# --------------------------------------------------------------------------- #
def _create_token(
    subject: Union[str, int],
    expires_delta: timedelta,
    token_type: str,
    extra: Dict[str, Any] | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    payload: Dict[str, Any] = {
        "sub": str(subject),
        "iat": now,
        "type": token_type,
        "exp": now + expires_delta,
        "jti": str(uuid4()),  # unique id
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)


def create_access_token(sub: Union[str, int], role: str) -> str:
    return _create_token(
        subject=sub,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        token_type="access",
        extra={"role": role},
    )


def create_refresh_token(sub: Union[str, int]) -> str:
    return _create_token(
        subject=sub,
        expires_delta=timedelta(days=7),
        token_type="refresh",
    )


def decode_token(token: str) -> Dict[str, Any]:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise ValueError("Invalid or expired token") from exc