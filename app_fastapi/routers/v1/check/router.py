from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.check import http_method

router = APIRouter(prefix=urls.CHECK_PREFIX)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.CHECK_TAG],
    name="check",
    # response_model=ResponseTest,
)(http_method.http_post)
