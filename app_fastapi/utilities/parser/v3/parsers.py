from app_fastapi.utilities.parser.v3.docx_parser.docx_parser import DocxParser

# from app_fastapi.utilities.parser.v3.pptx_parser.pptx_parser import PptxParser
# from app_fastapi.utilities.parser.v3.xlsx_parser.xlsx_parser import XlsxParser
# from app_fastapi.utilities.parser.v3.rtf_parser.rtf_parser import RtfParser


class Parsers:
    VERSION = "3"

    @classmethod
    def docx_parser(
        cls,
        input_file: bytes,
        ignore_paragraph_run: bool = False,
    ):
        return DocxParser(
            input_file=input_file, ignore_paragraph_run=ignore_paragraph_run
        )

    # @classmethod
    # def pptx_parser(
    #     cls,
    #     input_file: bytes,
    #     ignore_paragraph_run: bool = False,
    # ):
    #     return PptxParser(input_file=input_file, ignore_paragraph_run=ignore_paragraph_run)

    # @classmethod
    # def xlsx_parser(
    #     cls,
    #     input_file: bytes,
    #     ignore_paragraph_run: bool = False,
    # ):
    #     return XlsxParser(input_file=input_file, ignore_paragraph_run=ignore_paragraph_run)

    # @classmethod
    # def rtf_parser(
    #     cls,
    #     input_file: bytes,
    #     ignore_paragraph_run: bool = False,
    # ):
    #     return RtfParser(input_file=input_file, ignore_paragraph_run=ignore_paragraph_run)
