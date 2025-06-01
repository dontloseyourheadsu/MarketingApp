# apps/fastapi_app/core/deps.py
from typing import Annotated, List

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .database import get_db
from ..models.user import User
from ..services.user_service import get_user_by_id
from ..core.security import decode_token

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Query, Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

from fastapi import Request

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
    request: Request = Depends(),
) -> User:
    try:
        payload = decode_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise ValueError
    except ValueError:  # token invalid / missing sub
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user = get_user_by_id(db, int(user_id))
    if user is None or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")
    
    request.state.user_id = user.id
    return user


def require_roles(*roles: List[str]):  # usage: Depends(require_roles("owner", "admin"))
    def _role_guard(
        current_user: Annotated[User, Depends(get_current_user)],
    ) -> User:
        if current_user.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return current_user

    return _role_guard


# --------------------------------------------------------------------------- #
# Pagination dependency – keeps endpoints DRY                                 #
# --------------------------------------------------------------------------- #
from fastapi import Query


def pagination_params(
    skip: Annotated[int, Query(0, ge=0)],
    limit: Annotated[int, Query(100, ge=1, le=1000)],
):
    return {"skip": skip, "limit": limit}

def paginate(query: Query, skip: int, limit: int):
    total = query.order_by(None).count()
    items = query.offset(skip).limit(limit).all()
    return total, items


def add_pagination_headers(resp: JSONResponse, total: int, skip: int, limit: int):
    resp.headers["Content-Range"] = f"items {skip}-{skip+limit-1}/{total}"
    resp.headers["X-Total-Count"] = str(total)