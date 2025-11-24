from dataclasses import dataclass
from typing import Optional

@dataclass
class RefreshToken:
    id: int
    user_id: int
    token: str
    expires_at: str
    revoked: bool
