from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
# Создаём асинхронный движок для подключения к базе данных
engine = create_async_engine(DATABASE_URL, echo=True)
# Создаём фабрику сессий для взаимодействия с базой данных
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
