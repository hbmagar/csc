from typing import TYPE_CHECKING
from sqlmodel import Enum, Relationship, SQLModel, Field
from datetime import datetime, timezone

if TYPE_CHECKING:
    from .user import User
    from .order_item import OrderItem
    from .payment import Payment


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(SQLModel, table=True):
    __tablename__ = "orders"
    id: int | None = Field(default=None, primary_key=True)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    total_amount: float = Field(default=0.0, max_digits=10, precision=2, nullable=False)
    shipping_address: str = Field(nullable=False)
    billing_address: str = Field(nullable=False)

    status: OrderStatus = Field(default=OrderStatus.PENDING, nullable=False)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    )
    user_id: int = Field(foreign_key="users.id")

    # one to one relationships'
    user: "User" = Relationship(back_populates="orders")

    # one to many relationships'
    items: list["OrderItem"] = Relationship(back_populates="order")
    payments: list["Payment"] = Relationship(back_populates="order")
