import asyncio
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from langchain.prompts import PromptTemplate
import json, re

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


async def process_check_each(
    llm_client: Clients, idx: int, each: dict, prompt: PromptTemplate
):
    async with semaphore:
        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                if not each["result"]:
                    print("action")
                    chain = prompt | llm_client
                    response = await chain.ainvoke(
                        {
                            "korean": each["source"],
                            "chinese": each["target"],
                        }
                    )
                    match = re.search(
                        r"```json\n(.*?)\n```|(\{.*?\})", response.content, re.DOTALL
                    )
                    if match:
                        json_str = match.group(1) or match.group(2)
                        data = json.loads(json_str)

                        each["result"] = data["result"]
                        each["errors"] = data["errors"]

                return idx, each
            except Exception as e:
                print("=" * 100)
                print("Rate limit 초과 또는 다른 오류 발생: ", e)
                print(response.content)
                print("=" * 100)
                if "rate limit" in str(e).lower():
                    retry_count += 1
                    print(
                        f"잠시 {RATE_LIMIT_WAIT_TIME}초 대기 후 재시도합니다... (시도 {retry_count}/{MAX_RETRIES})"
                    )
                    await asyncio.sleep(RATE_LIMIT_WAIT_TIME)
                else:
                    print("오류가 발생하여 재시도를 중단합니다.")
                    return idx, each
