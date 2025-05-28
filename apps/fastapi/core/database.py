from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from ..core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
)

SessionLocal: sessionmaker[Session] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
ScopedSession = scoped_session(SessionLocal)


# Dependency
def get_db():
    db = ScopedSession()
    try:
        yield db
    finally:
        db.close()