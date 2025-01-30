from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.user import http_method

router = APIRouter(prefix=urls.USER_PREFIX)

router.get(
    path=urls.ENDPOINT + "/test",
    # tags=[tags.test],
    name="test",
    # response_model=ResponseTest,
)(http_method.http_get)