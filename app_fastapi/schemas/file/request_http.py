from fastapi import UploadFile
from pydantic import BaseModel, Field


class RequestHttpGet(BaseModel):
    limit_int: int = Field(20, ge=1)
    page_number: int = Field(1, ge=1)
