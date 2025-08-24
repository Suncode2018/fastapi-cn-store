# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

# นิยามตาราง Users
class User(Base):
    __tablename__ = "users" # ชื่อตารางในฐานข้อมูล

    # คอลัมน์ต่างๆ ในตาราง
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())