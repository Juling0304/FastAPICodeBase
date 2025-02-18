from langchain.prompts import PromptTemplate

suggest_prompt = PromptTemplate(
    input_variables=["korean_text", "keywords"],
    template="""
The text contains terms that were matched to a glossary, but the accuracy is very low because it simply lists the matched terms.
Please filter out the terms that do not match the context, such as incorrect keywords like "인," "대," "도," etc., which may have been matched erroneously.
Provide only the terms that are truly relevant to the content.
Provide the response in JSON format.
Please use double quotes (") instead of single quotes (') to comply with JSON rules.
Please provide the response in JSON format without wrapping it in an "Output" field. Instead, return it directly in the format shown in the example response

Example Input:
{{
"text": "기존의 교육과정은 태권도에 대한 핵심적인 지식과 정보를 제공하려 하였는데, 이것은 수강자들이 태권도에 대해서 모든 것을 처음 배운다는 불합리한 가정에 근거한 것이었습니다.",
"keywords": ['가정 - 家庭', '공 - 球', '과정 - 过程', '인 - 仁', '대 - 大', '도 - 道', '기 - 基', '핵심 - 核心', '가 - 家', '다 - Da', '한 - 一', '이 - 這', '근 - 艮', '배 - 肚子', '지식 - 知识', '수 - 數', '은 - 銀', '기존 - 過去', '처음 - 最初', '태 - 太', '태권 - 跆拳', '태권도 - 跆拳道', '근거 - 根據', '음 - 阴', '정 - 正', '불 - 火', '모든 - 所有的', '강 - 刚', '교육 - 教学', '정보 - 信息']
}}

Example response:
{{"keywords": ['가정 - 家庭', '과정 - 过程', '핵심 - 核心', '지식 - 知识', '기존 - 過去', '처음 - 最初', '태권 - 跆拳', '태권도 - 跆拳道', '근거 - 根據', '모든 - 所有的', '교육 - 教学', '정보 - 信息']}}


Input:
{{
"text": "{korean_text}",
"keywords": {keywords}
}}
""",
)
