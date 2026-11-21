from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator
from app.models.order import OrderStatus
from pydantic.alias_generators import to_camel


class CheckoutRequest(BaseModel):
    shipping_address: str


class OrderStatusUpdateRequest(BaseModel):
    status: OrderStatus


class OrderRead(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: OrderStatus
    shipping_address: str
    created_at: datetime
    items: list["OrderItemRead"] = []  # Forward reference to OrderItemRead

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class OrderItemRead(BaseModel):
    id: int
    product_id: int
    product_name: Optional[str] = Field(default=None, alias="productName")
    quantity: int
    unit_price: float
    is_reviewed: bool

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )

    @model_validator(mode="before")
    @classmethod
    def map_fields_from_relationships(cls, data):
        if hasattr(data, "product"):
            return {
                "id": data.id,
                "product_id": data.product_id,
                "product_name": data.product.name if data.product else "unknown",
                "quantity": data.quantity,
                "unit_price": data.unit_price,
                "is_reviewed": data.is_reviewed,
            }

        return data

    @computed_field
    def subtotal(self) -> Decimal:
        return self.quantity * self.unit_price
