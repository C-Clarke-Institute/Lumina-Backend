from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class CategoryCreate(BaseModel):

    name: str = Field(..., max_length=100)
    slug: str = Field(...,max_length=120)
    description: Optional[str] = Field(None,max_length=250)
    image:str | None = None
    is_active: bool = True


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    slug: Optional[str] = Field(None, max_length=120)
    description: Optional[str] = Field(None, max_length=250)
    image: Optional[str] | None = None
    is_active: Optional[bool] = None

class CategoryResponse(CategoryCreate):

    id : int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True
    )

