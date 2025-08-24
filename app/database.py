# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # เพิ่มส่วนนี้
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)

# สร้าง SessionLocal class สำหรับสร้าง session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()