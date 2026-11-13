from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime, timezone

if TYPE_CHECKING:
    from .user import User
    from .product import Product


class Review(SQLModel, table=True):
    __tablename__ = "reviews"
    id: int | None = Field(default=None, primary_key=True)
    rating: int = Field(default=0, ge=0, le=5, nullable=False)
    comment: str = Field(default="", nullable=True)
    username: str = Field(default="", nullable=False)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    product_id: int = Field(foreign_key="products.id", nullable=False)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    )

    Product: "Product" = Relationship(back_populates="reviews")
    User: "User" = Relationship(back_populates="reviews")
