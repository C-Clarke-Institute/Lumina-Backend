from decimal import Decimal

from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base
from app.core.mixins import TimestampMixin


class Product(Base, TimestampMixin):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str] = mapped_column(String(150))
    slug: Mapped[str] = mapped_column(String(180),unique=True)
    description: Mapped[str | None]
    brand: Mapped[str | None]
    sku: Mapped[str] =  mapped_column(String(50),unique=True)
    base_price: Mapped[Decimal] = mapped_column(Numeric(10,2))
    is_featured: Mapped[bool] = mapped_column(default=False)
    is_active:Mapped[bool] = mapped_column(default=True)
    category = relationship("Category",back_populates="products")