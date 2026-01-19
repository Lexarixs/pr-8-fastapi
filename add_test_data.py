from app.database import SessionLocal, engine, Base
from app.models import Category, Product

Base.metadata.create_all(bind=engine)
db = SessionLocal()


if db.query(Category).count() == 0:
    cat1 = Category(name="Фрукты")
    cat2 = Category(name="Овощи")
    db.add_all([cat1, cat2])
    db.commit()

    p1 = Product(name="Яблоко", price=100, category_id=cat1.id)
    p2 = Product(name="Банан", price=80, category_id=cat1.id)
    p3 = Product(name="Морковь", price=50, category_id=cat2.id)
    db.add_all([p1, p2, p3])
    db.commit()

db.close()
print("Тестовые данные добавлены!")
