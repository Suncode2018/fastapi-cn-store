# FastAPI CNStore Project  
(แดชบอร์ดรายงาน CN จากร้าน)  

## 📖 คำอธิบาย (Description)  
โปรเจกต์นี้เป็น **RESTful API** ที่พัฒนาด้วย **FastAPI** สำหรับใช้เป็น backend ของระบบแดชบอร์ดรายงาน CN จากร้าน โดยเชื่อมต่อกับฐานข้อมูล MSSQL ผ่าน SQLAlchemy รองรับการทำงานแบบ Asynchronous และมีเอกสาร API อัตโนมัติ  

## ✨ คุณสมบัติหลัก (Features)  
- 🚀 พัฒนาด้วย **FastAPI** ที่ให้ประสิทธิภาพสูง  
- 🗄️ เชื่อมต่อฐานข้อมูลด้วย **SQLAlchemy**  
- ⚡ รองรับการทำงานแบบ **Asynchronous**  
- 📑 เอกสาร API (Swagger UI และ ReDoc) สร้างขึ้นโดยอัตโนมัติ  

## 📋 ข้อกำหนดเบื้องต้น (Prerequisites)  
- **Python 3.11+** (ตามพาธ `D:\Python311\python.exe`)  
- MSSQL Database (พร้อม connection string)  

## ⚙️ การติดตั้ง (Installation)  

### 1. Clone repository  
```bash
git clone <your-repository-url>
cd fastapi-cn-store
```

### 2. ตั้งค่าสภาพแวดล้อม (Setup Environment)  

#### วิธีที่ 1: รันสคริปต์ `init.bat` (แนะนำสำหรับ Windows)  
```bash
init.bat
```
สคริปต์นี้จะทำการ:  
- สร้าง virtual environment (`venv`)  
- Activate virtual environment  
- อัปเกรด pip  
- ติดตั้ง dependencies จาก `requirements.txt`  

#### วิธีที่ 2: ทำด้วยตนเอง  
```bash
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔑 การตั้งค่า Environment Variables  
ให้สร้างไฟล์ `.env` ไว้ที่ root ของโปรเจกต์ โดยมีตัวอย่างดังนี้:  

```env
# Database connection string (ปรับให้ตรงกับ server ของคุณ)
DATABASE_URL=mssql+pyodbc://username:password@server_name/db_name?driver=ODBC+Driver+17+for+SQL+Server

# Secret key สำหรับ JWT หรือการเข้ารหัสอื่น ๆ
SECRET_KEY=your_secret_key_here

# Algorithm สำหรับ JWT
ALGORITHM=HS256

# Token expiration time (นาที)
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## ▶️ การรันแอปพลิเคชัน (Running the Application)  
หลังจากติดตั้งและ activate virtual environment แล้ว ให้รันเซิร์ฟเวอร์สำหรับพัฒนาได้ด้วย:  

```bash
uvicorn main:app --reload
uvicorn app.main:app --reload
```

- `main` คือชื่อไฟล์ Python (เช่น `main.py`)  
- `app` คืออ็อบเจกต์ FastAPI (เช่น `app = FastAPI()`)  
- `--reload` ทำให้เซิร์ฟเวอร์รีสตาร์ทอัตโนมัติเมื่อแก้ไขโค้ด  

## 🌐 Endpoints  
- **API Root** → [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
