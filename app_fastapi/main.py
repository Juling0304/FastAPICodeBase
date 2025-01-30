from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from app_fastapi.core.lifespans.lifespan import app_lifespan
from app_fastapi.configurations.configuration import origins, get_settings
from app_fastapi.routers.v1 import router as v1_router
# from app_fastapi.core.middlewares.http_logger import LoggingMiddleware

app = FastAPI(
    title="CodeBase",
    version="1.0.0",
    # lifespan=app_lifespan,
    servers=None,
    docs_url="/",

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(LoggingMiddleware)

app.include_router(v1_router.router)