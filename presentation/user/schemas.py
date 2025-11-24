from pydantic import BaseModel, EmailStr
from typing import Optional

class UserDTO(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Optional[str]
    instruction: Optional[str]

class CreateUserDTO(BaseModel):
    username: str
    email: EmailStr
    password: str
    gender: Optional[str]
    instruction: Optional[str]

