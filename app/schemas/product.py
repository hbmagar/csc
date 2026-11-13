from sqlmodel import SQLModel


class ProductCreate(SQLModel):
    name: str
    description: str
    price: float
    category_id: int
    