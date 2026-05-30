import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.database import engine, SessionLocal, Base
from app.models.user import User
from app.models.restaurant import Restaurant
from factories import UserFactory, RestaurantFactory, MenuItemFactory, OrderFactory

def seed_db():
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы/проверены.")

    with SessionLocal() as session:
        if session.query(Restaurant).first():
            print("База уже наполнена. Пропуск.")
            return

    print("Генерация тестовых данных...")
    
    restaurants = [RestaurantFactory() for _ in range(3)]
    users = [UserFactory() for _ in range(5)]
    menu_items = [MenuItemFactory() for _ in range(15)]
    orders = [OrderFactory() for _ in range(10)]
    
    print("База успешно наполнена!")

if __name__ == "__main__":
    seed_db()