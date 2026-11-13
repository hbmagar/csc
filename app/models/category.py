from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from .product import Product


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, nullable=False)
    description: Optional[str] = Field(default=None)

    # one to many relationships
    products: list["Product"] = Relationship(
        back_populates="category",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )
