from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.category.repository import CategoryRepository
from app.modules.category.schemas import CategoryResponse, CategoryCreate
from app.modules.category.service import CategoryService

router = APIRouter(prefix="/categories",tags=["Categories"])


def get_category_service(db:AsyncSession = Depends(get_db)) -> CategoryService:

    repository = CategoryRepository(db)

    return CategoryService(repository)


@router.post("/",response_model=CategoryResponse, status_code=201)
async def create_category(request: CategoryCreate,service: CategoryService = Depends(get_category_service)):
    return await service.create_category(request)