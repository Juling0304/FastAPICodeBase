import asyncio
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from langchain.prompts import PromptTemplate
import json

semaphore = asyncio.Semaphore(15)
RATE_LIMIT_WAIT_TIME = 30
MAX_RETRIES = 3


async def process_suggest_each(llm_client: Clients, each: dict, prompt: PromptTemplate):
    async with semaphore:
        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                print("action")
                chain = prompt | llm_client
                # response = await chain.ainvoke(**each)
                response = await chain.ainvoke(
                    {"korean_text": each["source"], "keywords": each["search"]}
                )
                content = response.content.replace("'", '"')
                res_dict = json.loads(content)
                each["suggest"] = res_dict["keywords"]
                return each
            except Exception as e:
                print("=" * 100)
                print("Rate limit 초과 또는 다른 오류 발생: ", str(e))
                print("=" * 100)
                if "rate limit" in str(e).lower():
                    retry_count += 1
                    print(
                        f"잠시 {RATE_LIMIT_WAIT_TIME}초 대기 후 재시도합니다... (시도 {retry_count}/{MAX_RETRIES})"
                    )
                    await asyncio.sleep(RATE_LIMIT_WAIT_TIME)
                else:
                    print("오류가 발생하여 재시도를 중단합니다.")
                    each["suggest"] = ""
                    return each
                each["suggest"] = ""
        return each
