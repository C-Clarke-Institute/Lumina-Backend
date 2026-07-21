from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.category.models import Category


class CategoryRepository:

    def __init__(self,db: AsyncSession):
        self.db = db

    async def create_category(self, category: Category) -> Category:

        self.db.add(category)
        await  self.db.commit()
        await self.db.refresh(category)
        return category

    async def get_all_category(self) -> list[Category]:
        result = await self.db.execute(select(Category))

        return result.scalars().all()

    async  def get_by_id(self,category_id:int) -> Optional[Category]:
        return await self.db.get(Category,category_id)

    async def get_by_name(self,name:str) -> Category:
        result = await self.db.execute(select(Category).where(Category.name == name))

        return result.scalar_one_or_none()

    async def update(self, category:Category) -> Category:
        await self.db.commit()
        await self.db.refresh(category)
        return category
    async  def delete(self,category:Category) -> None:
        await self.db.delete(category)
        await self.db.commit()