from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from escarpolette.settings import Config

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False)


def init_app(config: Config):
    engine = create_engine(
        config.DATABASE_URI, connect_args={"check_same_thread": False}
    )
    SessionLocal.configure(bind=engine)


def get_db():
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()
