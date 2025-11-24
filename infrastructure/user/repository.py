from typing import List, Optional
from sqlalchemy.orm import Session
import bcrypt

from infrastructure.user.models import UserModel
from application.user.mappers import model_to_entity, entity_to_dto, create_dto_to_entity
from presentation.user.schemas import CreateUserDTO, UserDTO

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_from_dto(self, dto: CreateUserDTO) -> UserDTO:
        user_entity = create_dto_to_entity(dto)
        model = UserModel(
            name=user_entity.username,
            email=user_entity.email,
            password_hash=user_entity.hashed_password,
            gender=user_entity.gender,
            language=user_entity.language,
            instruction=user_entity.instruction
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return entity_to_dto(model_to_entity(model))

    def get_by_id(self, id: int) -> Optional[UserDTO]:
        model = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not model:
            return None
        return entity_to_dto(model_to_entity(model))

    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def list(self, limit: int = 100, offset: int = 0) -> List[UserDTO]:
        models = self.db.query(UserModel).offset(offset).limit(limit).all()
        return [entity_to_dto(model_to_entity(m)) for m in models]

    def update(self, id: int, **kwargs) -> Optional[UserDTO]:
        model = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not model:
            return None
        if "password" in kwargs:
            model.password_hash = bcrypt.hashpw(kwargs.pop("password").encode(), bcrypt.gensalt()).decode()
        for k, v in kwargs.items():
            if hasattr(model, k):
                setattr(model, k, v)
        self.db.commit()
        self.db.refresh(model)
        return entity_to_dto(model_to_entity(model))

    def delete(self, id: int) -> bool:
        model = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True
