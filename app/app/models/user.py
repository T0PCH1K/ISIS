import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from typing import TYPE_CHECKING
from sqlalchemy import String, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.order import Order

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), unique=True)
    role: Mapped[str] = mapped_column(String(20), default="client", nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    
    orders: Mapped[list["Order"]] = relationship(back_populates="user", lazy="select")
    
    __table_args__ = (
        CheckConstraint("role IN ('client', 'courier', 'restaurant_admin', 'admin')", name="chk_user_role"),
    )