from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    instruction = Column(String, nullable=True)
    created_at = Column(String, nullable=False)

class UserAlertsModel(Base):
    __tablename__ = "user_alerts"
    user_id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer, primary_key=True, index=True)
    is_active = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False)
class UserPlanModel(Base):
    __tablename__ = "user_plan"
    user_id = Column(Integer, primary_key=True, index=True)
    date = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)

