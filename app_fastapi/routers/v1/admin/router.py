from fastapi import APIRouter

from app_fastapi.routers.v1 import urls, tags


router = APIRouter(prefix=urls.ADMIN_PREFIX)