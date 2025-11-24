from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RefreshTokenModel(Base):
    __tablename__ = "refresh_token"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    token = Column(String, unique=True, nullable=False)
    expires_at = Column(String, nullable=False)
    revoked = Column(Integer, nullable=False, default=0)