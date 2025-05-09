from fastapi import Depends, HTTPException, Query
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from typing import List
import os, asyncio, pandas as pd, json
from app_fastapi.utilities.parser.v3.parsers import Parsers as ParsersV3
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from app_fastapi.utilities.llm_util.v1.async_util import process_global_law_trans_each, process_global_law_check_each
from app_fastapi.prompts.editor_trans import e_trans_prompt, e_check_prompt, e_keyword_prompt


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

async def http_post_check(file: UploadFile = File(...),):
    """
    xlsx로 감수 프롬프트 작동
    """
    filename, extension = os.path.splitext(file.filename)
    excel_df = pd.read_excel(file.file, engine="openpyxl")

    excel_df["check"] = excel_df["check"].fillna("")
    json_str = excel_df.to_json(orient="records", force_ascii=False)
    list_data = json.loads(json_str)

    tasks = []
    llm_client = Clients.make_client("claude-3-7-sonnet-20250219")

    for each in list_data:
        if not each["check"]:
            tasks.append(process_global_law_check_each(llm_client, {"target":each["target"], "trans": each["trans"]}, e_check_prompt))

    if tasks:
        processed_data = await asyncio.gather(*tasks)
        updates_trans = {d['target']: d['trans'] for d in processed_data}
        updates_check = {d['target']: d['check'] for d in processed_data}

        excel_df.loc[excel_df['target'].isin(updates_trans.keys()), 'trans'] = excel_df['target'].map(updates_trans).fillna(excel_df['trans'])
        excel_df.loc[excel_df['target'].isin(updates_check.keys()), 'check'] = excel_df['target'].map(updates_check).fillna(excel_df['check'])

        excel_df.to_excel(f"storage/{filename}_check.xlsx", index=False)

    return True


async def http_post_keyword(file: UploadFile = File(...),):
    filename, extension = os.path.splitext(file.filename)
    excel_df = pd.read_excel(file.file, engine="openpyxl")
    target_text = '\n'.join(excel_df['target'].astype(str).tolist())
    trans_text = '\n'.join(excel_df['trans'].astype(str).tolist())

    
    llm_client = Clients.make_client("claude-3-7-sonnet-20250219")

    chain = e_keyword_prompt | llm_client
    response = await chain.ainvoke(
        {"target": target_text, "trans": trans_text}
    )
    content = response.content.replace("'", '"')
    res_dict = json.loads(content)
    print(res_dict)

    return True