# FastAPICodeBase

간단한 작업으로 FastAPI 코드 컨벤션 정리

app_fastapi
  - configurations : 환경 변수 등 설정 값
  - core : 핵심 기능 및 클래스
  - prompts : 프롬프트들
  - routers : 라우터들
  - schemas : 요청, 응답 스키마
  - utilities : 반복적으로 사용되는 기능들

app_celery
  - 작업 큐를 위한 celery (작업 전)

app_database
  - DB 관련 기능 (Redis, Query 등) (작업 전)