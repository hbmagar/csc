from sqlmodel import SQLModel, Field
from datetime import datetime, timedelta, timezone


class ResetCode(SQLModel, table=True):
    __tablename__ = "reset_codes"
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    code: str = Field(unique=True, index=True)

    expires_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    ) + timedelta(hours=5)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False,
    )
