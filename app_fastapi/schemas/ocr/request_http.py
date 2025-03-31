from fastapi import UploadFile
from pydantic import BaseModel, Field
from enum import Enum


class OCRType(str, Enum):
    Google = "google"
    Naver = "naver"
    Upstage = "upstage"
