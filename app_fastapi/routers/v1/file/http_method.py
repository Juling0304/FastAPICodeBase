from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.parser.v3.parsers import Parsers as ParsersV3


async def http_post(
    file: UploadFile = File(...),
):
    """
    docx 파일 텍스트 추출
    """
    full_string_list = []

    filename_extension: str = file.filename.split(".")[-1]
    file_data = await file.read()

    parsers = ParsersV3

    if filename_extension.lower() == "docx":
        parser = parsers.docx_parser(file_data)
    else:
        raise HTTPException(status_code=500, detail={"detail": "Error"})

    original_processed_parsing_data_list = (
        parser.get_original_processed_parsing_data_list()
    )

    for original_processed_parsing_data in original_processed_parsing_data_list:
        full_string_list.append(original_processed_parsing_data.get_sentence().strip())

    # 공백 제거
    full_string = "".join(full_string_list)

    print(full_string)
    return True
