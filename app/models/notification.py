from typing import TYPE_CHECKING
from sqlmodel import Enum, SQLModel, Field
from datetime import datetime, timezone


class NotificationStatus(str, Enum):
    WELCOME = "welcome"
    ORDER_UPDATED = "order_updated"
    PAYMENT_UPDATED = "payment_updated"
    PROMOTIONAL = "promotional"
    SECURITY = "security"


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"
    id: int | None = Field(default=None, primary_key=True)

    # Destination email address i.e where are you want send the notification
    recipient_email: str = Field(index=True, nullable=False)
    title: str = Field(nullable=False)
    message: str = Field(nullable=False)
    notification_type: NotificationStatus = Field(
        default=NotificationStatus.ORDER_UPDATED, nullable=False
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    )
