from domain.user.entity import User
from infrastructure.user.models import UserModel
from presentation.user.schemas import UserDTO, CreateUserDTO
import bcrypt
from typing import Optional

def model_to_entity(m: UserModel) -> User:
    return User(
        id=m.id,
        username=m.name,
        email=m.email,
        hashed_password=m.password_hash,
        gender=m.gender,
        language=m.language,
        instruction=m.instruction,
        created_at=m.created_at
    )

def entity_to_dto(e: User) -> UserDTO:
    return UserDTO(
        id=e.id,
        username=e.username,
        email=e.email,
        gender=e.gender,
        language=e.language,
        instruction=e.instruction,
        created_at=e.created_at
    )

def create_dto_to_entity(dto: CreateUserDTO) -> User:
    hashed = bcrypt.hashpw(dto.password.encode(), bcrypt.gensalt()).decode()

    return User(
        id = None,
        username=dto.username,
        email=dto.email,
        hashed_password=hashed,
        gender=dto.gender,
        language=dto.language,
        instruction=dto.instruction,
        created_at=None
    )
