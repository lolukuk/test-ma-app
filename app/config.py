import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Определяем URL-адреса базы данных и облачного API
DATABASE_URL = os.getenv("DATABASE_URL")
CLOUD_API_URL = os.getenv("CLOUD_API_URL")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")