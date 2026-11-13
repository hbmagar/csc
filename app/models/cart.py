from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from .user import User
    from .product import Product


class Cart(SQLModel, table=True):
    __tablename__ = "carts"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True, nullable=False)

    # one to many relationships'
    user: "User" = Relationship(back_populates="cart")
    items: list["CartItem"] = Relationship(back_populates="cart")


class CartItem(SQLModel, table=True):
    __tablename__ = "cart_items"
    id: int | None = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="carts.id")
    product_id: int = Field(foreign_key="products.id")
    quantity: int = Field(default=1, nullable=False)

    # one to many relationships'
    cart: "Cart" = Relationship(back_populates="items")
    product: "Product" = Relationship(back_populates="cart_items")

    # one to many relationships'
    user: "User" = Relationship(back_populates="cart")
    items: list["CartItem"] = Relationship(back_populates="cart")
