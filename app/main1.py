from db.db import SessionLocal
from db import crud

def main():
    """Главная функция программы"""
    
    print("=" * 50)
    print("📚 КНИЖНЫЙ КАТАЛОГ")
    print("=" * 50)
    
    # Создание сессии
    db = SessionLocal()
    
    try:
        # Получение всех категорий
        categories = crud.get_categories(db)
        
        if not categories:
            print("❌ В базе данных нет категорий!")
            print("   Запустите init_db.py для заполнения базы данных.")
            return
        
        print(f"\n📂 Найдено категорий: {len(categories)}\n")
        
        # Вывод книг по категориям
        for category in categories:
            print(f"📁 КАТЕГОРИЯ: {category.title}")
            print("-" * 40)
            
            # Получаем книги для этой категории
            books = crud.get_books_by_category(db, category.id)
            
            if not books:
                print("   📭 Нет книг в этой категории")
            else:
                for book in books:
                    print(f"   📖 {book.title}")
                    if book.description:
                        print(f"      📝 {book.description}")
                    print(f"      💰 Цена: {book.price} ₽")
                    if book.url:
                        print(f"      🔗 {book.url}")
                    print()
            
            print("-" * 40)
            print()
        
        # Статистика
        all_books = crud.get_books(db)
        print(f"\n📊 Всего книг в каталоге: {len(all_books)}")
        
    except Exception as e:
        print(f"❌ Ошибка при работе с базой данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()