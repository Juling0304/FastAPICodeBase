from fastapi import Depends, HTTPException, Body
from typing import Annotated, Dict, Optional
from pywebpush import webpush, WebPushException
from app_fastapi.configurations.configuration import get_settings


async def http_post(
    # db: database_dependency,
    # current_user: Dict = Depends(verify_access_token),
    sub_info: Dict = Body(...)
):
    """
    테스트
    """
    print("test")
    webpush(
        subscription_info=sub_info,
        data="알림입니다.",
        vapid_private_key=get_settings().VAPID_PRIVATE_KEY,
        vapid_claims={"sub":"mailto:kwkim@eqqui.com"}
    )
    return True