from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional


async def http_get(
    # db: database_dependency,
    # current_user: Dict = Depends(verify_access_token),
    test: Optional[str] = None,
):
    """
    테스트
    """
    print("test")
    return True