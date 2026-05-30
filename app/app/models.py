from datetime import datetime
from sqlalchemy import String, Integer, Float, Boolean, DateTime, ForeignKey, CheckConstraint, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="client")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    orders: Mapped[list["Order"]] = relationship(back_populates="user", lazy="select")
    __table_args__ = (CheckConstraint("role IN ('client','courier','restaurant_admin','admin')", name="chk_user_role"),)

class Restaurant(Base):
    __tablename__ = "restaurants"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    rating: Mapped[float] = mapped_column(default=0.0)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    menu_items: Mapped[list["MenuItem"]] = relationship(back_populates="restaurant", lazy="select")

class MenuItem(Base):
    __tablename__ = "menu_items"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    is_available: Mapped[bool] = mapped_column(default=True, nullable=False)
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_items")
    __table_args__ = (CheckConstraint("price > 0", name="chk_menu_price"),)

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="new")
    total_amount: Mapped[float] = mapped_column(nullable=False)
    delivery_address: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    user: Mapped["User"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(back_populates="order", lazy="select", cascade="all, delete-orphan")
    __table_args__ = (
        CheckConstraint("status IN ('new','confirmed','cooking','ready','on_the_way','delivered','cancelled')", name="chk_order_status"),
        CheckConstraint("total_amount > 0", name="chk_order_total"),
    )

class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1, nullable=False)
    price_at_order: Mapped[float] = mapped_column(nullable=False)
    order: Mapped["Order"] = relationship(back_populates="items")
    __table_args__ = (CheckConstraint("quantity > 0", name="chk_item_quantity"),)