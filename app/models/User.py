from sqlalchemy import Column, Text, String, TIMESTAMP, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class UserType(enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = 'users'

    student_id    = Column(Text, primary_key=True)
    name          = Column(Text, nullable=False)
    cpf           = Column(String(11), nullable=False, unique=True)
    email         = Column(Text, nullable=False, unique=True)
    hash_password = Column(Text, nullable=False)
    user_type     = Column(Enum(UserType), nullable=False)
    created_at    = Column(TIMESTAMP, nullable=False, default=datetime.now)

    def to_json(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "cpf": self.cpf,
            "email": self.email,
            "user_type": self.user_type.value,
            "created_at": self.created_at
        }