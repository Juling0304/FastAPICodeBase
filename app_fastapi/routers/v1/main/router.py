from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.main import http_method

router = APIRouter(prefix=urls.MAIN_PREFIX)

router.get(path=urls.ENDPOINT_SLASH, tags=[tags.MAIN_TAG], name="Index")(http_method.http_get)
