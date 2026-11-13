from pydantic import ConfigDict
from sqlmodel import SQLModel
from typing import Optional


class CategoryCreate(SQLModel):
    name: str
    description: Optional[str] = None

class CategoryRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None
    model_config = ConfigDict(
        exclude_none=True 
     ) # automatically convert snake_case to camelCase e.g


class CategoryUpdate(SQLModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None

