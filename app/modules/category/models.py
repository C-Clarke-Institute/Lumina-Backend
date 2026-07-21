from typing import TYPE_CHECKING

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base
from app.core.mixins import TimestampMixin

if TYPE_CHECKING:
     from app.modules.product.models import Product

class Category(Base,TimestampMixin):

    __tablename__ = "categories"

    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True,nullable=False)
    slug: Mapped[str] = mapped_column(String(120),unique=True,nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(255),nullable=True)
    image: Mapped[str|None] = mapped_column(String(255),nullable=True)
    is_active:Mapped[bool] = mapped_column(Boolean,default=True, nullable=False)
    products: Mapped[list["Product"]] = relationship(back_populates="category")