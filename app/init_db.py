from db.db import SessionLocal, engine, Base
from db import models, crud

def init_database():
    """Инициализация базы данных"""
    
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы")
    
    db = SessionLocal()
    
    try:
        categories = [
            "Программирование",
            "Художественная литература",
            "Научная фантастика"
        ]
        
        for cat_title in categories:
            existing = crud.get_category_by_title(db, cat_title)
            if not existing:
                category = crud.create_category(db, cat_title)
                print(f"Создана категория: {category.title}")
            else:
                print(f"ℹКатегория уже существует: {cat_title}")
        
        prog_cat = crud.get_category_by_title(db, "Программирование")
        fiction_cat = crud.get_category_by_title(db, "Художественная литература")
        sci_fi_cat = crud.get_category_by_title(db, "Научная фантастика")
        
        books_data = [
            {"title": "Python. Изучаем программирование", 
             "description": "Книга по Python для начинающих", 
             "price": 1500.0, "url": "", "category_id": prog_cat.id},
            {"title": "Алгоритмы: построение и анализ", 
             "description": "Классический учебник по алгоритмам", 
             "price": 2000.0, "url": "", "category_id": prog_cat.id},
            {"title": "Чистый код", 
             "description": "Как писать хороший код", 
             "price": 1800.0, "url": "", "category_id": prog_cat.id},
            {"title": "Изучаем SQL", 
             "description": "Базы данных для начинающих", 
             "price": 1300.0, "url": "", "category_id": prog_cat.id},
            
            {"title": "Преступление и наказание", 
             "description": "Роман Фёдора Достоевского", 
             "price": 800.0, "url": "", "category_id": fiction_cat.id},
            {"title": "Война и мир", 
             "description": "Эпопея Льва Толстого", 
             "price": 900.0, "url": "", "category_id": fiction_cat.id},
            
            {"title": "Дюна", 
             "description": "Фантастический роман Фрэнка Герберта", 
             "price": 1200.0, "url": "", "category_id": sci_fi_cat.id},
            {"title": "Автостопом по галактике", 
             "description": "Юмористическая фантастика", 
             "price": 1100.0, "url": "", "category_id": sci_fi_cat.id},
        ]
        
        for book_data in books_data:

            existing_books = crud.get_books(db)
            if not any(b.title == book_data["title"] for b in existing_books):
                book = crud.create_book(db, **book_data)
                print(f"Создана книга: {book.title}")
            else:
                print(f"Книга уже существует: {book_data['title']}")
        
        print("\n Инициализация базы данных завершена!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()