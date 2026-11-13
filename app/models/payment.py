from typing import TYPE_CHECKING
from sqlmodel import Enum, Relationship, SQLModel, Field
from datetime import datetime, timezone
from app.models.order import Order

if TYPE_CHECKING:
    from .order import Order


class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class Payment(SQLModel, table=True):
    __tablename__ = "payments"
    id: int | None = Field(default=None, primary_key=True)
    amount: float = Field(default=0.0, max_digits=10, precision=2, nullable=False)
    currency: str = Field(default="NPR", nullable=False)
    provider_transaction_id: str = Field(index=True, nullable=False, unique=True)
    payment_method: str
    status: PaymentStatus = Field(default=PaymentStatus.PENDING, nullable=False)

    Order_id: int = Field(foreign_key="orders.id", unique=False, nullable=False)
    order: "Order" = Relationship(back_populates="payments")

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    )
