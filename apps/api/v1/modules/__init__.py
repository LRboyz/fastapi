from fastapi import APIRouter
from .book_api.book import router as book_router

router = APIRouter()

router.include_router(prefix="/book", router=book_router, tags=['book'])
