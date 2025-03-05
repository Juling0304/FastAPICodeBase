from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.etc.save_chunks_to_files import save_chunks_to_files
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from app_fastapi.utilities.llm_util.v1.async_util import process_suggest_each
from langchain.schema.runnable import RunnableSequence
from app_fastapi.prompts.suggest_keyword import suggest_prompt
import os, pandas as pd, json, asyncio


async def http_post(
    file: UploadFile = File(...),
):
    """
    업로드 엑셀 내용 읽어 용어 서치
    """

    keyword_df = pd.read_csv("storage/keyword/ko_cn_keyword.csv", encoding="utf-8")
    excel_df = pd.read_excel(file.file, engine="openpyxl")

    keyword_dict = dict(
        zip(
            keyword_df["한국어"],
            [
                f"{ko} - {cn}"
                for ko, cn in zip(keyword_df["한국어"], keyword_df["중국어"])
            ],
        )
    )

    excel_df["search"] = excel_df["source"].apply(
        lambda source: [
            ko_cn for ko, ko_cn in keyword_dict.items() if ko in str(source)
        ]
    )

    search_df = excel_df[excel_df["search"].notna()]
    json_str = search_df.to_json(orient="records", force_ascii=False)
    list_data = json.loads(json_str)

    llm_client = Clients.client_openai("gpt-3.5-turbo-1106")
    tasks = [
        process_suggest_each(llm_client, each, suggest_prompt) for each in list_data
    ]
    processed_data = await asyncio.gather(*tasks)

    for each in processed_data:
        del each["search"]

    down_df = pd.DataFrame(processed_data)

    down_df.to_excel("storage/suggest_test.xlsx", index=False)

    return True
