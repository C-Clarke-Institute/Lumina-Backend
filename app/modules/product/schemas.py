from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    category_id:int
    name:str = Field(...,max_length=150)
    slug:str = Field(...,max_length=180)
    description:str | None = None
    brand :str | None = None
    sku: str = Field(...,max_length=50)
    base_price: Decimal
    is_featured : bool = False
    is_active: bool = True

class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = Field(None, max_length=150)
    slug: Optional[str] = Field(None, max_length=180)
    description: Optional[str]  = None
    brand: Optional[str] = None
    sku: Optional[str] = Field(None, max_length=50)
    base_price: Optional[Decimal] = None
    is_featured: Optional[bool] = None
    is_active: Optional[bool] = None

class ProductResponse(BaseModel):
    id : int
    category_id:int
    name:str
    slug:str
    description: str | None
    brand: str | None
    sku : str
    base_price : Decimal
    is_featured: bool
    is_active: bool
    created_at: datetime
    updated_at : datetime | None

    model_config = ConfigDict(
        from_attributes=True
    )



