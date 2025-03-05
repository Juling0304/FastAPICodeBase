from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from app_fastapi.configurations.configuration import get_settings


class Clients:
    VERSION = "1"

    @classmethod
    def client_openai(cls, model: str):
        return ChatOpenAI(
            model=model,
            temperature=0.7,
            openai_api_key=get_settings().GPT_API_KEY,
        )

    @classmethod
    def client_anthropic(cls, model: str):
        return ChatAnthropic(
            model=model,
            temperature=0.7,
            # max_tokens=200,
            api_key=get_settings().CLAUDE_API_KEY,
        )
