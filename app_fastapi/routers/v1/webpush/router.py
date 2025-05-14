from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.webpush import http_method

router = APIRouter(prefix=urls.WEBPUSH_PREFIX)

router.post(
    path=urls.ENDPOINT + "/test",
    tags=["webpush"],
    name="test",
    # response_model=ResponseTest,
)(http_method.http_post)