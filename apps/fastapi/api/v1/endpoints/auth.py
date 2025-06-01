from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Form, Response
from sqlalchemy.orm import Session

from ....core.config import settings
from ....core.database import get_db
from ....core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from ....schemas.token import Token
from ....services.user_service import authenticate_user, get_user_by_id
from ....services.token_service import save_refresh_token, revoke_token, is_token_revoked

router = APIRouter()

@router.post("/login", response_model=Token)
def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access = create_access_token(user.id, user.role)
    refresh = create_refresh_token(user.id)

    # store refresh in DB
    payload = decode_token(refresh)
    save_refresh_token(db, payload)

    # send refresh token as httpOnly cookie
    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        secure=False,               # set True behind HTTPS
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
        path="/api/v1/auth/refresh",
    )
    return {"access_token": access, "token_type": "bearer"}


@router.post("/refresh", response_model=Token)
def refresh_token(response: Response, refresh_token: str | None = None, db: Session = Depends(get_db)):
    """
    Called either via Cookie (preferred) or in body {refresh_token:"..."} for tooling.
    """
    token = refresh_token
    if token is None:
        raise HTTPException(status_code=400, detail="refresh_token missing")

    payload = decode_token(token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=400, detail="Not a refresh token")

    jti = payload["jti"]
    if is_token_revoked(db, jti):
        raise HTTPException(status_code=401, detail="Token revoked")

    user = get_user_by_id(db, int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # rotate refresh token
    revoke_token(db, jti)
    new_refresh = create_refresh_token(user.id)
    save_refresh_token(db, decode_token(new_refresh))

    response.set_cookie(
        key="refresh_token",
        value=new_refresh,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
        path="/api/v1/auth/refresh",
    )

    new_access = create_access_token(user.id, user.role)
    return {"access_token": new_access, "token_type": "bearer"}


@router.post("/logout", status_code=204)
def logout(refresh_token: str | None = None, db: Session = Depends(get_db)):
    """
    Revoke the refresh token (passed via cookie or body) and implicitly
    invalidates the linked access token on the client side.
    """
    if refresh_token:
        try:
            payload = decode_token(refresh_token)
            revoke_token(db, payload["jti"])
        except ValueError:
            pass