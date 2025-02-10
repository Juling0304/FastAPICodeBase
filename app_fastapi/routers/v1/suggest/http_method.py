from fastapi import Depends, HTTPException
from typing import Annotated, Dict, Optional
from app_fastapi.configurations.configuration import get_settings
from fastapi import UploadFile, File
from app_fastapi.utilities.parser.v3.parsers import Parsers as ParsersV3
from app_fastapi.utilities.etc.save_chunks_to_files import save_chunks_to_files
import os, pandas as pd


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
            keyword_df["중국어"],
            [
                f"{ko} - {cn}"
                for ko, cn in zip(keyword_df["한국어"], keyword_df["중국어"])
            ],
        )
    )

    excel_df["matched_ko"] = excel_df["target"].apply(
        lambda target: ",".join(
            [ko_cn for cn, ko_cn in keyword_dict.items() if cn in target]
        )
    )

    excel_df.to_excel("storage/suggest_test.xlsx", index=False)

    return True
