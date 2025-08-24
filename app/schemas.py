# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

# --- Schema สำหรับรับข้อมูลตอนสร้าง User ---
# ไม่ต้องรับ id หรือ created_at จาก user
class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str | None = None # | None คือ Optional

# --- Schema สำหรับส่งข้อมูลกลับไปให้ User ---
# เป็น Schema พื้นฐานที่ใช้แสดงข้อมูล User
class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str | None = None
    created_at: datetime

    # บอก Pydantic ให้อ่านข้อมูลจาก ORM model ได้เลย
    class Config:
        from_attributes = True # ใน Pydantic v1 คือ orm_mode = True