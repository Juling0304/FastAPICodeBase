from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.suggest import http_method

router = APIRouter(prefix=urls.SUGGEST_PREFIX)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.SUGGEST_TAG],
    name="suggest",
    # response_model=ResponseTest,
)(http_method.http_post)
