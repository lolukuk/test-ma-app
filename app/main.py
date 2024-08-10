from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from uuid import uuid4
from app.models import FileMetadata, Base
from app.database import SessionLocal, engine
from app.cloud import upload_to_cloud
import aiofiles
import os

app = FastAPI()


# Создание таблиц
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Загрузка файла
@app.post("/upload/")
async def upload_file(file: UploadFile):
    uid = str(uuid4())
    file_location = f"files/{uid}_{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    file_metadata = FileMetadata(
        uid=uid,
        filename=file.filename,
        extension=file.filename.split(".")[-1],
        format=file.content_type,
        size=len(content),
        path=file_location
    )

    async with SessionLocal() as session:
        session.add(file_metadata)
        await session.commit()

    await upload_to_cloud(file_location)
    return {"uid": uid}


# Получение файла по UID
@app.get("/file/{uid}/")
async def get_file(uid: str):
    async with SessionLocal() as session:
        file_metadata = await session.get(FileMetadata, uid)
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(path=file_metadata.path, filename=file_metadata.filename)
