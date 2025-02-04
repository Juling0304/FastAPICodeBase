from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.parser.v3.parsers import Parsers as ParsersV3
from app_fastapi.utilities.etc.save_chunks_to_files import save_chunks_to_files
import os


async def http_post(
    file: UploadFile = File(...),
):
    """
    docx 파일 텍스트 추출
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
    full_string = "".join(full_string_list)

    print(len(full_string))
    save_chunks_to_files(
        full_string,
        filename,
    )
    return True
