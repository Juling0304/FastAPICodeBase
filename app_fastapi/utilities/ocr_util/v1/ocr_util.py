import os, uuid, time, json, requests
from typing import List
from google.cloud import documentai_v1beta3 as documentai
from app_fastapi.configurations.configuration import get_settings


class OCR_API_CLASS_BASE:
    def __init__(self):
        pass

    def response(self, target):
        raise NotImplementedError("Subclasses should implement this method")

    def summary(self, json_dict: dict):
        raise NotImplementedError("Subclasses should implement this method")

    def run_process(self, target: str) -> List:
        return self.summary(self.response(target))


class Upstage(OCR_API_CLASS_BASE):
    def __init__(self, api_key: str, url: str, task: str) -> None:
        self.task = task
        self.url = url + "/" + self.task
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def response(self, target):
        files = {"document": open(target, "rb")}
        return requests.post(self.url, headers=self.headers, files=files).json()

    def summary(self, json_dict: dict) -> List:
        summary_lst = []
        if self.task == "layout-analysis":
            for i in json_dict["elements"]:
                summary_lst.append(
                    {
                        "coords": i["bounding_box"],
                        "text": i["text"],
                        "page": str(i["page"]),
                    }
                )

        elif self.task == "ocr":
            for page in json_dict["pages"]:
                for word in page["words"]:

                    summary_lst.append(
                        {
                            "coords": word["boundingBox"]["vertices"],
                            "text": word["text"],
                            "page": str(page["id"] + 1),
                        }
                    )
        return summary_lst


class Naver(OCR_API_CLASS_BASE):
    def __init__(self, url: str, secret_key: str) -> None:
        self.url = url
        request_json = {
            "images": [{"format": "jpg", "name": "demo"}],
            "requestId": str(uuid.uuid4()),
            "version": "V2",
            "timestamp": int(round(time.time() * 1000)),
        }
        self.payload = {"message": json.dumps(request_json).encode("UTF-8")}
        self.headers = {"X-OCR-SECRET": secret_key}

    def response(self, target):
        files = [("file", open(target, "rb"))]
        return requests.post(
            self.url, headers=self.headers, data=self.payload, files=files
        ).json()

    def summary(self, json_dict: dict) -> List:
        summary_lst = []
        for page, i in enumerate(json_dict["images"]):
            for j in i["fields"]:
                summary_lst.append(
                    {
                        "coords": j["boundingPoly"]["vertices"],
                        "text": j["inferText"],
                        "page": str(page + 1),
                    }
                )
        # print(summary_lst)
        return summary_lst


class Google(OCR_API_CLASS_BASE):
    def __init__(self, project_id: str, location: str, processor_id: str) -> None:
        self.project_id = project_id
        self.location = location
        self.processor_id = processor_id
        self.client = documentai.DocumentProcessorServiceClient()

    def response(self, target):
        with open(target, "rb") as f:
            image_content = f.read()

        name = f"projects/{self.project_id}/locations/{self.location}/processors/{self.processor_id}"

        ext = (os.path.splitext(target)[-1]).replace(".", "")

        if ext == "pdf":  # pdf file
            mime_type = "application/pdf"
        elif ext == "png":  # png file
            mime_type = "image/png"
        else:  # jpg file, jpeg file
            mime_type = "image/jpeg"

        document = {"content": image_content, "mime_type": mime_type}
        request = {"name": name, "document": document}

        return self.client.process_document(request=request)

    def summary(self, input_data) -> List:
        summary_lst = []

        full_text = input_data.document.text
        for page in input_data.document.pages:
            for block in page.blocks:
                coords = [
                    {"x": vertex.x, "y": vertex.y}
                    for vertex in block.layout.bounding_poly.vertices
                ]
                for i in block.layout.text_anchor.text_segments:
                    text = full_text[i.start_index : i.end_index]

                ### 기존코드 ###
                """
                summary_lst.append({
                            "coords": coords,
                            "text": text,
                            "page": page.page_number
                    })
                """

                ### 241223_수정사항(SSG) ###
                """
                구글엔진의 경우, text 안에 "\n"이 들어가 있어서 줄바꿈이 아닌 경우 발생
                "\n"로 나눠서 리스트에 추가하는 방식으로 변경
                """
                split_text = text.split("\n")
                for j in range(len(split_text)):
                    summary_lst.append(
                        {
                            "coords": coords,
                            "text": split_text[j],
                            "page": page.page_number,
                        }
                    )
        # print(summary_lst)

        return summary_lst


def call_API(ocr: str):
    if ocr == "google":
        return Google(
            project_id=get_settings().GOOGLE_OCR_PROJECT_ID,
            processor_id=get_settings().GOOGLE_OCR_PROCESSOR_ID,
            location=get_settings().GOOGLE_OCR_LOCATION,
        )
    elif ocr == "naver":
        return Naver(
            url=get_settings().NAVER_OCR_URL,
            secret_key=get_settings().NAVER_OCR_SECRET_KEY,
        )
    elif ocr == "upstage":
        return Upstage(
            api_key=get_settings().UPSTAGE_OCR_API_KEY,
            url=get_settings().UPSTAGE_OCR_URL,
            task="ocr",
        )
    else:
        return None
