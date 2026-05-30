from app.database import engine, SessionLocal, Base
from app.models.restaurant import Restaurant
from app.models.menu_item import OrderFactory
from app.models.order import Restaurant
from app.models.user import UserFactory
from factories import RestaurantFactory, MenuItemFactory

def seed_db():
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы/проверены.")

    with SessionLocal() as session:
        if session.query(Restaurant).first():
            print("База уже наполнена. Пропуск.")
            return

        print("Генерация тестовых данных...")
        for _ in range(3): RestaurantFactory()
        for _ in range(5): UserFactory()
        for _ in range(15): MenuItemFactory()
        for _ in range(10): OrderFactory()
        session.commit()
        print("База успешно наполнена!")

if __name__ == "__main__":
    seed_db()