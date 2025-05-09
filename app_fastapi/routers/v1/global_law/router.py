from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags
from app_fastapi.routers.v1.global_law import http_method

router = APIRouter(prefix=urls.GL_PREFIX)

router.post(
    path=urls.ENDPOINT,
    tags=[tags.GL_TAG],
    name="global_law",
    # response_model=ResponseTest,
)(http_method.http_post)
router.post(
    path=urls.RETRY,
    tags=[tags.GL_TAG],
    name="global_law_retry",
    # response_model=ResponseTest,
)(http_method.http_post_retry)
router.post(
    path=urls.CHECK_PREFIX,
    tags=[tags.GL_TAG],
    name="global_law_check",
    # response_model=ResponseTest,
)(http_method.http_post_check)
router.post(
    path=urls.KEYWORD_PREFIX,
    tags=[tags.GL_TAG],
    name="global_law_check",
    # response_model=ResponseTest,
)(http_method.http_post_keyword)