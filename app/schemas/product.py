from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from pydantic.alias_generators import to_camel

from app.schemas.review import ReviewResponse


class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock_quantity: int
    category_id: int
    image_url: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class ProductDetail(ProductRead):
    reviews: List["ReviewResponse"] = []


class ProductUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    category_id: Optional[int] = None
    image_url: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )
