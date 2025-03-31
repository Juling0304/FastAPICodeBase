from fastapi import Depends, HTTPException, Query
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from app_fastapi.schemas.ocr.request_http import OCRType
from app_fastapi.utilities.ocr_util.v1.ocr_util import call_API
from fastapi import UploadFile, File


async def http_post(ocr: OCRType = Query(...)):
    """
    미리 업로드 된 이미지 파일 OCR로 전체 추출 작업
    """
    if ocr == "google":
        print("구글")

    ocr_api = call_API(ocr)

    return True
