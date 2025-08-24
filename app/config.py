# app/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str  # กำหนดให้รับแค่ database_url ตัวเดียวเท่านั้น

    class Config:
        env_file = ".env"

settings = Settings()