import factory
from faker import Faker
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import engine
from app.models.user import User
from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem
from app.models.order import Order

fake = Faker("ru_RU")

Session = scoped_session(sessionmaker(bind=engine))

class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

class UserFactory(BaseFactory):
    class Meta: 
        model = User
    
    phone = factory.LazyFunction(lambda: fake.phone_number()[:20])
    name = factory.LazyFunction(lambda: fake.first_name()[:100])
    role = "client"

class RestaurantFactory(BaseFactory):
    class Meta: 
        model = Restaurant
    
    name = factory.LazyFunction(lambda: f"Ресторан {fake.company()}"[:150])
    address = factory.LazyFunction(lambda: fake.address()[:255])
    rating = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=3.0, max_value=5.0), 1))

class MenuItemFactory(BaseFactory):
    class Meta: 
        model = MenuItem
    
    restaurant = factory.SubFactory(RestaurantFactory)
    name = factory.LazyFunction(lambda: f"{fake.word().capitalize()} {fake.word()}"[:100])
    price = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=200, max_value=1500), 2))
    description = factory.LazyFunction(lambda: fake.sentence()[:500])
    is_available = True

class OrderFactory(BaseFactory):
    class Meta: 
        model = Order
    
    user = factory.SubFactory(UserFactory)
    restaurant = factory.SubFactory(RestaurantFactory)
    status = "new"
    total_amount = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=500, max_value=5000), 2))
    delivery_address = factory.LazyFunction(lambda: fake.address()[:255])