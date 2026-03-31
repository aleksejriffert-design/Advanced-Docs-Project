from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="LibraryAPI",
    description="Интерактивная документация системы управления библиотекой",
    version="1.0.0"
)

# Модель данных для книги (Pydantic)
class Book(BaseModel):
    id: int
    title: str = Field(..., example="1984")
    author: str = Field(..., example="George Orwell")
    is_available: bool = True

# Имитация базы данных
db = [
    {"id": 1, "title": "C# in Depth", "author": "Jon Skeet", "is_available": True}
]

@app.get("/books", response_model=List[Book], summary="Получить список всех книг")
def get_books():
    """
    Возвращает полный список книг, доступных в библиотеке.
    """
    return db

@app.post("/books", status_code=201, summary="Добавить новую книгу")
def add_book(book: Book):
    """
    Добавляет новую книгу в базу данных. 
    Требует ID, название и автора.
    """
    db.append(book.dict())
    return {"message": f"Книга '{book.title}' успешно добавлена"}

@app.get("/books/{book_id}", summary="Поиск книги по ID")
def get_book(book_id: int):
    book = next((item for item in db if item["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book