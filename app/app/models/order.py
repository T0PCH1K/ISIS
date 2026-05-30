from typing import TYPE_CHECKING
from sqlalchemy import String, Float, ForeignKey, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.restaurant import Restaurant
    from app.models.menu_item import MenuItem

class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="new", nullable=False)
    total_amount: Mapped[float] = mapped_column(nullable=False)
    delivery_address: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    
    user: Mapped["User"] = relationship(back_populates="orders")
    restaurant: Mapped["Restaurant"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        lazy="select",
        cascade="all, delete-orphan"
    )
    
    __table_args__ = (
        CheckConstraint("status IN ('new', 'confirmed', 'cooking', 'ready', 'on_the_way', 'delivered', 'cancelled')", name="chk_order_status"),
        CheckConstraint("total_amount > 0", name="chk_order_total_positive"),
    )

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1, nullable=False)
    price_at_order: Mapped[float] = mapped_column(nullable=False)
    
    # Строковые ссылки
    order: Mapped["Order"] = relationship(back_populates="items")
    menu_item: Mapped["MenuItem"] = relationship(back_populates="order_items")
    
    __table_args__ = (
        CheckConstraint("quantity > 0", name="chk_item_quantity_positive"),
    )