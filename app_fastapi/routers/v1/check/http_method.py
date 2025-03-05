from fastapi import Depends, HTTPException, Query
from typing import Annotated, Dict, Optional, Union
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.etc.save_chunks_to_files import save_chunks_to_files
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from app_fastapi.utilities.llm_util.v1.async_util import (
    process_check_each,
)
from langchain.schema.runnable import RunnableSequence
from app_fastapi.prompts.check_ko_cn import (
    check_ko_cn_prompt_v1,
    check_ko_cn_prompt_v2,
    check_ko_cn_prompt_v3,
    check_ko_cn_prompt_v4,
)
from app_fastapi.schemas.llm_list import SelectModel
from typing import Union, Annotated
import os, pandas as pd, json, asyncio


async def http_post(file: UploadFile = File(...), llm_model: SelectModel = Query(...)):
    """
    업로드 엑셀 내용 읽어 감수 작업
    """
    filename, extension = os.path.splitext(file.filename)
    excel_df = pd.read_excel(file.file, engine="openpyxl")

    excel_df["suggest"] = excel_df["suggest"].fillna("").replace("", "[]")
    json_str = excel_df.to_json(orient="records", force_ascii=False)
    list_data = json.loads(json_str)

    llm_client = Clients.make_client(llm_model)

    tasks = [
        process_check_each(llm_client, idx, each, check_ko_cn_prompt_v4)
        for idx, each in enumerate(list_data)
    ]
    processed_data = await asyncio.gather(*tasks)

    processed_data_sorted = sorted(processed_data, key=lambda x: x[0])
    processed_data_sorted = [x[1] for x in processed_data_sorted]
    print("gather finish")

    down_df = pd.DataFrame(processed_data)

    down_df.to_excel(f"storage/{filename}_check.xlsx", index=False)

    return True
