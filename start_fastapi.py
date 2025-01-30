import sys
import uvicorn
from app_fastapi.configurations.configuration import get_settings

if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) == 0:
        if get_settings().APP_ENV != "prod":
            print("start with reload")
            uvicorn.run(
                "app_fastapi.main:app",
                reload=True,
                log_level="debug",
                host="0.0.0.0",
                port=get_settings().API_PORT,
            )
        else:
            print("start with worker")
            uvicorn.run(
                "app_fastapi.main:app",
                workers=4,
                log_level="debug",
                host="0.0.0.0",
                port=get_settings().API_PORT,
            )
