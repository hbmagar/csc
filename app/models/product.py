from typing import Optional, TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime, timezone

if TYPE_CHECKING:
    from .category import Category
    from .order_item import OrderItem
    from .review import Review


class Product(SQLModel, table=True):
    __tablename__ = "products"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, nullable=False)
    description: Optional[str] = Field(default=None)
    price: float = Field(default=0.0, max_digits=10, precision=2, nullable=False)
    stock_quantity: int = Field(default=0, nullable=False)
    image_url: Optional[str] = Field(default=None)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
    category_id: int = Field(foreign_key="categories.id")

      # one to one relationships'
    category: "Category" = Relationship(back_populates="products")

    # one to many relationships'
    order_items: list["OrderItem"] = Relationship(back_populates="product")
    reviews: list["Review"] = Relationship(
        back_populates="product", 
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}   )