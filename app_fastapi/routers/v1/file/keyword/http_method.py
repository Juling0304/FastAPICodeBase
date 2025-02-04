from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.llm_util.v1.llm_util import Clients
from langchain.schema.runnable import RunnableSequence
from app_fastapi.prompts.extract_keyword import prompt as extract_prompt
import os, json


async def http_post():
    """
    테스트
    """
    chunk_files = sorted(os.listdir("storage/chunks"))
    print(chunk_files)

    full_chunk = ""
    for each in chunk_files:
        if each.endswith(".txt"):  # Check if the file is a .txt file
            file_path = os.path.join("storage/chunks", each)
            with open(file_path, "r", encoding="utf-8") as f:
                full_chunk = f.read()

            client = Clients.client_openai()
            chain = extract_prompt | client
            response = chain.invoke({"long_text": full_chunk})
            print(response.content)
            print(type(response.content))
            res_dict = json.loads(response.content)
            print(res_dict)
        break
    # client = Clients.client_openai()

    # from langchain.prompts import PromptTemplate

    # prompt = PromptTemplate(
    #     input_variables=["long_text"],
    #     template=extract_prompt,
    # )

    # chain = prompt | client
    # response = chain.invoke({"topic": "사과"})

    # print(response)
    return True
