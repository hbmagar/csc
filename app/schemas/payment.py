from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CheckOutSessionRequest(BaseModel):
    order_it: int

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )


class CheckOutSessionResponse(BaseModel):
    checkout_url: str
    session_id: str

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True,
        exclude_none=True,
    )
