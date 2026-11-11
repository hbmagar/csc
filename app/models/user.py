
from enum import Enum
from alembic.environment import Optional
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime, timezone



class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    DELIVERY="DELIVERY"


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    profile_picture: Optional[str] = Field(default=None)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    role: UserRole = Field(default=UserRole.CUSTOMER, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # one to many relationships
    order: list["Order"] = Relationship(back_populates="user")
    reviews: list["Reviews"] = Relationship(back_populates="user")
    carts: Optional["Carts"] = Relationship(back_populates="user")