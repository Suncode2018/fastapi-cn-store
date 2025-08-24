# app/main.py

# 1. นำเข้า (Import) Library ที่จำเป็น
from fastapi import FastAPI  # นำเข้าคลาสหลักของ FastAPI
from typing import List      # นำเข้าประเภทข้อมูล List สำหรับ type hinting (แม้จะยังไม่ได้ใช้ในโค้ดนี้ แต่เป็นการเตรียมพร้อมที่ดี)

from . import schemas       # นำเข้าโมดูล schemas จากในโฟลเดอร์ app เดียวกัน (ใช้ . แทนชื่อโฟลเดอร์ปัจจุบัน)

# 2. สร้าง Instance ของ FastAPI
app = FastAPI()             # สร้างอ็อบเจกต์แอปพลิเคชันหลัก ซึ่งจะเป็นจุดศูนย์กลางของ API ทั้งหมด

# 3. สร้าง Endpoint (หรือ Route)
@app.get("/")               # สร้าง "path operation decorator"
                            # @app.get บอกว่าฟังก์ชันข้างล่างนี้จะจัดการกับ HTTP GET request
                            # "/" คือ "path" หรือ URL ที่จะรับ request นี้ (ในที่นี้คือ URL รากสุดของเว็บ)
def read_root():            # ฟังก์ชันที่จะทำงานเมื่อมี request มาที่ path นี้
    return {"message": "Welcome to FastAPI CN Store"} # สิ่งที่ฟังก์ชันนี้ return จะถูกแปลงเป็น JSON response ส่งกลับไปให้ผู้ใช้