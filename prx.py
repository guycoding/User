from pydantic import BaseModel,SecretStr,EmailStr,validator,Field,field_validator
from typing import Literal
from uuid import uuid4,UUID
from enum import Enum
import json
import bcrypt
class Role(str,Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id:UUID=Field(default_factory=uuid4)
    name:str
    last_name:str
    password:SecretStr
    email:EmailStr
    role:Role
    gender:Literal["male","female"]


    class Config:
        use_enum_values = True


    @field_validator("password")
    def password_len_val(cls,password:SecretStr)->SecretStr:
        plain_password = password.get_secret_value()
        if len(plain_password)<8:
            raise ValueError("password must be 8 characters or longer")
        return password
    @field_validator("password", mode="after")
    def hash_salt_password(cls,password:SecretStr)->SecretStr:
        plain_password = password.get_secret_value()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(plain_password.encode(),salt)
        return  SecretStr(hashed_password.decode())
    def verify_password(self,input_password:str)->bool:
        return bcrypt.checkpw(input_password.encode(),self.password.get_secret_value().encode())


create_user ={"name":"charles","role":"user","last_name":"mosena","gender":"male","password":"858dghj54","email":"charlesmouzen@gmail.com"}

user = User(**create_user)
print(user.model_dump_json())
print(user.password.get_secret_value())
print(user.verify_password("858dghj54"))