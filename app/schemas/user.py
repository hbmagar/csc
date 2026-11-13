from sqlmodel import SQLModel
from pydantic import ConfigDict, EmailStr
from pydantic.alias_generators import to_camel
from typing import TYPE_CHECKING, Optional
from app.models.user import UserRole


class UserCreate(SQLModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[UserRole] = UserRole.CUSTOMER


class UserRead(SQLModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    active: bool
    profile_image: Optional[str] = None
    address: Optional[str] = None

    model_config = ConfigDict(
        alias_generator=to_camel,  # automatically convert snake_case to camelCase e.g. user_name -> userName
        populate_by_name=True,  # allow population of model by field name or alias
        from_attributes=True,  # allow population of model from ORM objects
    )


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class TokenData(SQLModel):
    token: str
    type: str = "bearer"
    user: UserRead


class UserUpdate(SQLModel):
    name: Optional[str] = None
    address: Optional[str] = None


class PasswordUpdate(SQLModel):
    old_password: str
    new_password: str

    model_config = ConfigDict(
        alias_generator=to_camel,  # automatically convert snake_case to camelCase e.g. user_name -> userName
        populate_by_name=True,  # allow population of model by field name or alias
        from_attributes=True,  # allow population of model from ORM objects
    )


class ForgotPasswordRequest(SQLModel):
    email: EmailStr


class ResetPasswordRequest(SQLModel):
    code: str
    new_password: str
