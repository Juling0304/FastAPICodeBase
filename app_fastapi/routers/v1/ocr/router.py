from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.ocr import http_method

router = APIRouter(prefix=urls.OCR_PREFIX)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.OCR_TAG],
    name="ocr",
    # response_model=ResponseTest,
)(http_method.http_post)
