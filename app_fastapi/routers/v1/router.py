from fastapi import APIRouter

from app_fastapi.routers.v1 import urls

from app_fastapi.routers.v1.admin import router as admin_router
from app_fastapi.routers.v1.user import router as user_router
from app_fastapi.routers.v1.main import router as main_router
from app_fastapi.routers.v1.file import router as file_router
from app_fastapi.routers.v1.suggest import router as suggest_router
from app_fastapi.routers.v1.check import router as check_router
from app_fastapi.routers.v1.ocr import router as ocr_router


router = APIRouter(prefix=urls.API_V1_ROUTER_PREFIX)

router.include_router(main_router.router)
router.include_router(admin_router.router)
router.include_router(user_router.router)
router.include_router(file_router.router)
router.include_router(suggest_router.router)
router.include_router(check_router.router)
router.include_router(ocr_router.router)
