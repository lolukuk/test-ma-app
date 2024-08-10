from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Модель для бд
class FileMetadata(Base):
    __tablename__ = "file_metadata"

    uid = Column(String, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    extension = Column(String, nullable=False)
    format = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    path = Column(String, nullable=False)
