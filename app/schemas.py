from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    """Базовая схема категории"""
    title: str

class CategoryCreate(CategoryBase):
    """Схема для создания категории"""
    pass

class CategoryUpdate(BaseModel):
    """Схема для обновления категории"""
    title: Optional[str] = None

class CategoryResponse(CategoryBase):
    """Схема для ответа с категорией"""
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    """Базовая схема книги"""
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    """Схема для создания книги"""
    pass

class BookUpdate(BaseModel):
    """Схема для обновления книги"""
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    """Схема для ответа с книгой"""
    id: int

    class Config:
        orm_mode = True