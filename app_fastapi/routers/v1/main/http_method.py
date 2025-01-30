from fastapi import HTTPException


async def http_get():
    try:
        pass

    except HTTPException as e:
        raise e

    return {"message": "TransCreation 2.0"}
