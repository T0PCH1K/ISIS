import factory
from faker import Faker
from app.database import SessionLocal
from app.models import User, Restaurant, MenuItem, Order

fake = Faker("ru_RU")

class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = SessionLocal
        sqlalchemy_session_persistence = "commit"

class UserFactory(BaseFactory):
    class Meta: model = User
    phone = factory.LazyFunction(fake.phone_number)
    name = factory.LazyFunction(fake.first_name)
    role = "client"

class RestaurantFactory(BaseFactory):
    class Meta: model = Restaurant
    name = factory.LazyFunction(lambda: f"Ресторан {fake.company()}")
    address = factory.LazyFunction(fake.address)
    rating = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=3.0, max_value=5.0), 1))

class MenuItemFactory(BaseFactory):
    class Meta: model = MenuItem
    restaurant = factory.SubFactory(RestaurantFactory)
    name = factory.LazyFunction(lambda: f"{fake.word().capitalize()} {fake.word()}")
    price = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=200, max_value=1500), 2))
    description = factory.LazyFunction(fake.sentence)

class OrderFactory(BaseFactory):
    class Meta: model = Order
    user = factory.SubFactory(UserFactory)
    restaurant = factory.SubFactory(RestaurantFactory)
    status = "new"
    total_amount = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=500, max_value=5000), 2))
    delivery_address = factory.LazyFunction(fake.address)