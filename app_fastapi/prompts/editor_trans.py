from langchain.prompts import PromptTemplate

e_trans_prompt = PromptTemplate(
    input_variables=["input","keyword"],
    template="""영어를 한국어로 번역해주세요.
아래 번역 지침을 따라서 번역해주세요.

'''번역지침

1. 조항의 제목은 괄호 안에 넣어 주세요. 
2. 원문에 없는 단어는 번역문에 추가하지 말아 주세요.
3. 원문에 있는 단어를 번역문에서 누락하지 말아 주세요.
4. 용어집이 있으면 용어를 수정하지 말고 그대로 정확히 적용하고 1번부터 순서대로 적용해 주세요.
5. 각 조항 앞의 번호는 원문의 형태 그대로 유지해 주세요.
6. 번역문을 한국의 법률 문투로 수정하고 조항의 제목은 괄호 안에 넣어 주세요. 
7. 번역문에서는 각주 표시를 삭제해 주세요.

답변은 JSON 형식에 따라주세요.
JSON의 key값은 trans로 고정하되, value에 변역된 문장을 넣어주세요.

용어집:
{keyword}

응답 예시:
{{"trans": "번역된 문장"}}

입력:
{input}
""",
)