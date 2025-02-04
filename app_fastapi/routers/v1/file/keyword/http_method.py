from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File


async def http_post(
    file: UploadFile = File(...),
):
    """
    테스트
    """

    print("keyword")
    return True
