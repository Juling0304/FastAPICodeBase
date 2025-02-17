from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from langchain.schema.runnable import RunnableSequence
from app_fastapi.prompts.extract_keyword import (
    cn_prompt as extract_cn_prompt,
    ko_prompt as extract_ko_prompt,
    en_prompt as extract_en_prompt,
)
import os, json
import pandas as pd


async def http_post_cn():
    """
    테스트
    """
    chunk_files = sorted(os.listdir("storage/chunks"))

    full_chunk = ""
    all_dict = {}
    i = 0
    for each in chunk_files:
        print(each)
        if each.endswith(".txt"):
            file_path = os.path.join("storage/chunks", each)
            with open(file_path, "r", encoding="utf-8") as f:
                full_chunk = f.read()

            client = Clients.client_openai()
            chain = extract_cn_prompt | client
            response = chain.invoke({"long_text": full_chunk})
            try:
                res_dict = json.loads(response.content)
            except:
                print("재작업 필요")
                res_dict = {}
            all_dict.update(res_dict)
            # print(all_dict)
        # if i >= 76:
        #     break

        # i += 1

    if all_dict:
        df = pd.DataFrame(list(all_dict.items()), columns=["중국어", "한국어"])

        df.to_excel("storage/chunks/keyword_cn.xlsx", index=False)

    return True


async def http_post_ko():
    """
    테스트
    """
    chunk_files = sorted(os.listdir("storage/chunks"))

    full_chunk = ""
    all_dict = {}
    i = 0
    for each in chunk_files:
        print(each)
        if each.endswith(".txt"):
            file_path = os.path.join("storage/chunks", each)
            with open(file_path, "r", encoding="utf-8") as f:
                full_chunk = f.read()

            client = Clients.client_openai()
            chain = extract_ko_prompt | client
            response = chain.invoke({"long_text": full_chunk})
            try:
                res_dict = json.loads(response.content)
            except:
                print("재작업 필요")
                res_dict = {}
            all_dict.update(res_dict)
            # print(all_dict)
        # if i >= 10:
        #     break

        # i += 1

    if all_dict:
        df = pd.DataFrame(list(all_dict.items()), columns=["중국어", "한국어"])

        df.to_excel("storage/chunks/keyword_ko.xlsx", index=False)

    return True


async def http_post_en():
    """
    테스트
    """
    chunk_files = sorted(os.listdir("storage/chunks"))

    full_chunk = ""
    all_dict = {}
    i = 0
    for each in chunk_files:
        print(each)
        if each.endswith(".txt"):
            file_path = os.path.join("storage/chunks", each)
            with open(file_path, "r", encoding="utf-8") as f:
                full_chunk = f.read()

            client = Clients.client_openai()
            chain = extract_en_prompt | client
            response = chain.invoke({"long_text": full_chunk})
            try:
                res_dict = json.loads(response.content)
            except:
                print("재작업 필요")
                res_dict = {}
            all_dict.update(res_dict)
            # print(all_dict)
        # if i >= 10:
        #     break

        # i += 1

    if all_dict:
        df = pd.DataFrame(list(all_dict.items()), columns=["영어", "한국어"])

        df.to_excel("storage/chunks/keyword_en.xlsx", index=False)

    return True
