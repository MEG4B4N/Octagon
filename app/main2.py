from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import books, categories
from app.db.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(categories.router)

@app.get("/health", tags=["health"])
def health_check():
    """Проверка работоспособности сервиса"""
    return {"status": "ok", "message": "Book API is running!"}

@app.get("/", tags=["root"])
def root():
    """Корневой эндпоинт"""
    return {
        "message": "Welcome to Book API!",
        "docs": "/docs",
        "health": "/health"
    }