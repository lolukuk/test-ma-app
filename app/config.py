import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CLOUD_API_URL = os.getenv("CLOUD_API_URL")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")
