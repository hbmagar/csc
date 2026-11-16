from pydantic import BaseModel, ConfigDict
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    model_config = ConfigDict(
        exclude_none=True 
     ) # automatically convert snake_case to camelCase e.g


class CategoryUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None

