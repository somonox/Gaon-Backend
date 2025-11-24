from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    password_hash: str
    name: str
    language: str
    gender: Optional[str]
    instruction: Optional[str]
    created_at: str

@dataclass
class UserAlerts:
    user_id: int
    type: int
    is_active: bool
    created_at: str

@dataclass
class UserPlan:
    user_id: int
    date: str
    title: str
    description: str
    created_at: str
    updated_at: str

