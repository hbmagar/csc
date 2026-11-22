from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from sqlmodel import Field
from datetime import datetime


class ReviewCreate(BaseModel):
    product_id: int
    rating: int = Field(ge=1, le=5)
    coomment: str

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class ReviewResponse(BaseModel):
    id: int
    rating: int
    comment: str
    username: str
    created_at: datetime
    product_id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )
