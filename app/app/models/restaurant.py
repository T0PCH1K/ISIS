import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from typing import TYPE_CHECKING
from sqlalchemy import String, Float, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.menu_item import MenuItem
    from app.models.order import Order

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    
    menu_items: Mapped[list["MenuItem"]] = relationship(
        back_populates="restaurant", 
        lazy="select",
        cascade="all, delete-orphan"
    )
    
    # Используем строковую ссылку "Order"
    orders: Mapped[list["Order"]] = relationship(
        back_populates="restaurant",
        lazy="select"
    )