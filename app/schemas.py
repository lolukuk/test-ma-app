from pydantic import BaseModel

class FileResponseSchema(BaseModel):
    uid: str
    filename: str
    extension: str
    format: str
    size: int

    class Config:
        orm_mode = True
