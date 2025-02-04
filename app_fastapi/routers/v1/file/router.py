from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.file import http_method
from app_fastapi.routers.v1.file.keyword import router as keyword_router

router = APIRouter(prefix=urls.FILE_PREFIX)

router.include_router(keyword_router.router)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.FILE_TAG],
    name="file",
    # response_model=ResponseTest,
)(http_method.http_post)
