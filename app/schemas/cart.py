from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CartRead(BaseModel):
    id: int
    user_id: int
    items: list[CartItemRead]
    total_quantity: int
    total_price: Decimal

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class CartItemRead(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_price: Decimal
    product_image: Optional[str]
    quantity: int
    subtotal: Decimal

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int = 1

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )
