from typing import TYPE_CHECKING
from sqlalchemy import String, Float, Boolean, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.restaurant import Restaurant
    from app.models.order import OrderItem

class MenuItem(Base):
    __tablename__ = "menu_items"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey("restaurants.id"), 
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
 
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_items")
    
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="menu_item",
        lazy="select"
    )
    
    __table_args__ = (
        CheckConstraint("price > 0", name="chk_menu_price_positive"),
    )