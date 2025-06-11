from pydantic import BaseModel, EmailStr, Field, SecretStr, validator,field_validator
from typing import Literal
from uuid import UUID, uuid4
from datetime import date
from enum import Enum
import bcrypt  # For password hashing

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    last_name: str
    password: SecretStr  # Hides password in logs & serialization
    email: EmailStr
    gender: Literal["male", "female"]
    role: Role
    date_of_birth: date

    class Config:
        use_enum_values = True  # Serializes Role.admin → "admin"

    from pydantic import constr

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, password: SecretStr) -> SecretStr:
        plain_password = password.get_secret_value()
        if len(plain_password) < 8:
            raise ValueError("Password must be at least 8 characters")
        return password


    @field_validator("password")
    @classmethod
    def hash_password(cls, password: SecretStr) -> SecretStr:
            plain_password = password.get_secret_value()
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
            return SecretStr(hashed_password.decode())  # Return as string for storage

    # Method to verify a password
    def verify_password(self, input_password: str) -> bool:
        return bcrypt.checkpw(
            input_password.encode(),
            self.password.get_secret_value().encode()
        )

create_user ={"name":"charles","role":"user","last_name":"mosena","gender":"male","password":"858dghj54","email":"charlesmouzen@gmail.com","date_of_birth":"1997-05-15"}

user = User(**create_user)
print(user.model_dump_json())
print(user.password.get_secret_value())
print(user.verify_password("858dghj54"))