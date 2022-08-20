from .models.book import Book
from fastapi import APIRouter
from apps.core.responses.json_response import Success
from .schema.book import BookInSerializer, BookSerializer


router = APIRouter()

@router.post("", response_model=BookSerializer)
async def create_book(book: BookInSerializer):
    book = Book(
        title=book.title,
        content=book.content,
    )
    await book.commit()
    book = book.dump()
    return Success(result=book, message="图书创建成功！")
