from langchain_openai import ChatOpenAI
from app_fastapi.configurations.configuration import get_settings


class Clients:
    VERSION = "1"

    @classmethod
    def client_openai(cls):
        return ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=get_settings().GPT_API_KEY,
        )
