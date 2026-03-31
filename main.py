"""
Модуль LibraryAPI.

Данный модуль предоставляет программный интерфейс (API) для управления 
библиотечным фондом, включая операции получения списка книг, 
добавления новых записей и поиска по идентификатору.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="LibraryAPI",
    description="Интерактивная документация системы управления библиотекой",
    version="1.0.0"
)

class Book(BaseModel):
    """
    Модель данных книги.
    
    Описывает структуру объекта книги, используемую при передаче данных 
    между клиентом и сервером.
    """
    id: int = Field(..., description="Уникальный идентификатор книги")
    title: str = Field(..., example="1984", description="Название произведения")
    author: str = Field(..., example="George Orwell", description="Автор книги")
    is_available: bool = Field(True, description="Статус доступности книги в архиве")

# Имитация базы данных
db = [
    {"id": 1, "title": "C# in Depth", "author": "Jon Skeet", "is_available": True}
]

@app.get("/books", response_model=List[Book], summary="Получить список всех книг")
def get_books():
    """
    Возвращает полный список книг, доступных в библиотеке.
    
    Метод извлекает все записи из временного хранилища данных.
    """
    return db

@app.post("/books", status_code=201, summary="Добавить новую книгу")
def add_book(book: Book):
    """
    Добавляет новую книгу в базу данных библиотеки.
    
    Принимает объект Book, валидирует его и сохраняет в список.
    """
    db.append(book.dict())
    return {"message": f"Книга '{book.title}' успешно добавлена"}

@app.get("/books/{book_id}", response_model=Book, summary="Поиск книги по ID")
def get_book(book_id: int):
    """
    Выполняет поиск конкретной книги по её уникальному идентификатору.
    
    Если книга с указанным ID не найдена, возвращает ошибку 404.
    """
    book = next((item for item in db if item["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book