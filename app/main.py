# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import SessionLocal, engine, Base

# --- สร้างตาราง (ถ้ายังไม่มี) ---
Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- Dependency สำหรับจัดการ Database Session ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoint สำหรับสร้าง User ---
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # สร้าง ORM model object จากข้อมูลที่รับมา
    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name
    )
    db.add(db_user) # เพิ่ม object ใหม่เข้าสู่ session
    db.commit()      # commit การเปลี่ยนแปลงลงฐานข้อมูล
    db.refresh(db_user) # refresh object เพื่อให้มีข้อมูลล่าสุดจาก DB (เช่น id)
    return db_user

# --- Endpoint สำหรับดึงข้อมูล User ทั้งหมด ---
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


# --- Endpoint เก่าของคุณ ---
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CN Store"}

@app.get("/test-db")
def test_database_connection():
    # ... (โค้ดเดิม) ...
    # เราสามารถลบ endpoint นี้ออกได้แล้วถ้าไม่ต้องการ
    pass