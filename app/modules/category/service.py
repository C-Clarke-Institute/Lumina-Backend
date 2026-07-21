from app.modules.category.models import Category
from app.modules.category.repository import CategoryRepository
from app.modules.category.schemas import CategoryCreate


class CategoryService:

    def __init__(self,repository: CategoryRepository):
        self.repository = repository

    async def  create_category(self,request:CategoryCreate) -> Category:
         existing_name = await self.repository.get_by_name(request.name)

         if existing_name:
             raise ValueError("Category name already exists.")

         category = Category(**request.model_dump())

         return await self.repository.create_category(category)

    async def get_all(self):
        return await self.repository.get_all_category()
