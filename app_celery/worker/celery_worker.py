import os

from celery import Celery
from celery.signals import worker_shutdown

from app_fastapi.configurations.configuration import get_settings


celery_worker_app_broker_url = f"redis://{get_settings().REDIS_HOST_NAME}:{get_settings().REDIS_PORT}/0"

celery_worker_app = Celery(
    __name__,
    broker=celery_worker_app_broker_url,
)

celery_worker_app.conf.update(
    broker_connection_retry_on_startup=True
)


@celery_worker_app.task(name="test")
def add(x, y):
    return x + y