from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from .product import Product
    from .order import Order


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"
    id: int | None = Field(default=None, primary_key=True)
    quantity: int = Field(default=1, nullable=False)
    unit_price: float = Field(default=0.0, max_digits=10, precision=2, nullable=False)
    is_reviewed: bool = Field(default=False, nullable=False)

    order_id: int = Field(foreign_key="orders.id")
    product_id: int = Field(foreign_key="products.id")

    # one to many relationships'
    order: "Order" = Relationship(back_populates="items")
    product: "Product" = Relationship(back_populates="order_items")
