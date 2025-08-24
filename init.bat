@echo off
REM Create virtual environment, install requirements, and init DB
"D:\Python311\python.exe" -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

echo Initialization complete!
pause
