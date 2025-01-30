from fastapi import APIRouter

from app_fastapi.routers.v1 import urls

from app_fastapi.routers.v1.admin import router as admin_router
from app_fastapi.routers.v1.user import router as user_router
from app_fastapi.routers.v1.main import router as main_router


router = APIRouter(prefix=urls.API_V1_ROUTER_PREFIX)

router.include_router(main_router.router)
router.include_router(admin_router.router)
router.include_router(user_router.router)
