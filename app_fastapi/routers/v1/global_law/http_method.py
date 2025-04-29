from fastapi import Depends, HTTPException, Query
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from typing import List
import os, asyncio, pandas as pd, json
from app_fastapi.utilities.parser.v3.parsers import Parsers as ParsersV3
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from app_fastapi.utilities.llm_util.v1.async_util import process_global_law_trans_each
from app_fastapi.prompts.editor_trans import e_trans_prompt


async def http_post(file: UploadFile = File(...),):
    """
    박 에디터님의 요청 프로세스 처리 (docx 초기)
    """
    full_string_list = []

    filename, extension = os.path.splitext(file.filename)

    file_data = await file.read()

    parsers = ParsersV3

    if extension.lower() == ".docx":
        parser = parsers.docx_parser(file_data)
    else:
        raise HTTPException(status_code=500, detail={"detail": "Error"})

    original_processed_parsing_data_list = (
        parser.get_original_processed_parsing_data_list()
    )

    for original_processed_parsing_data in original_processed_parsing_data_list:
        full_string_list.append(original_processed_parsing_data.get_sentence().strip())

    # 공백 제거
    # full_string = "".join(full_string_list)
    print(full_string_list)

    llm_client = Clients.make_client("claude-3-7-sonnet-20250219")
    tasks = [
        process_global_law_trans_each(llm_client, {"target":each}, e_trans_prompt) for each in full_string_list
    ]

    # tasks = [process_global_law_trans_each(llm_client, {"target": full_string_list[0]}, e_trans_prompt)]
    processed_data = await asyncio.gather(*tasks)

    # print(processed_data)
    down_df = pd.DataFrame(processed_data)

    down_df.to_excel(f"storage/{filename}_global_trans_test.xlsx", index=False)

    return True


async def http_post_retry(file: UploadFile = File(...),):
    """
    docx -> xlsx 이 후 빈 칸들 재시도를 위한 기능
    """
    filename, extension = os.path.splitext(file.filename)
    excel_df = pd.read_excel(file.file, engine="openpyxl")

    excel_df["trans"] = excel_df["trans"].fillna("")
    json_str = excel_df.to_json(orient="records", force_ascii=False)
    list_data = json.loads(json_str)

    tasks = []
    llm_client = Clients.make_client("claude-3-7-sonnet-20250219")

    for each in list_data:
        if not each["trans"]:
            tasks.append(process_global_law_trans_each(llm_client, {"target":each["target"]}, e_trans_prompt))
    if tasks:
        processed_data = await asyncio.gather(*tasks)

        updates_dict = {d['target']: d['trans'] for d in processed_data}
        excel_df.loc[excel_df['target'].isin(updates_dict.keys()), 'trans'] = excel_df['target'].map(updates_dict).fillna(excel_df['trans'])

        excel_df.to_excel(f"storage/{filename}_retry.xlsx", index=False)

    return True