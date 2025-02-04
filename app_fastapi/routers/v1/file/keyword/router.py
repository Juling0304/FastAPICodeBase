from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.file.keyword import http_method

router = APIRouter(prefix=urls.FILE_PREFIX + urls.KEYWORD_PREFIX)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.KEYWORD_TAG],
    name="keyword",
    # response_model=ResponseTest,
)(http_method.http_post)
