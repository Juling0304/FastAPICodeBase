from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from app_fastapi.configurations.configuration import get_settings
from app_fastapi.schemas.llm_list import SelectModel


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

    @classmethod
    def make_client(cls, llm_model: SelectModel):
        if "gpt" in llm_model:
            return cls.client_openai(llm_model)
        elif "claude" in llm_model:
            return cls.client_anthropic(llm_model)
        else:
            raise ValueError(f"Unsupported model: {llm_model}")
