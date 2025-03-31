from langchain.prompts import PromptTemplate

suggest_prompt = PromptTemplate(
    input_variables=["korean_text", "keywords"],
    template="""
The text contains terms that were matched to a glossary, but the accuracy is very low because it simply lists the matched terms.
Please filter out the terms that do not match the context, such as incorrect keywords like "인," "대," "도," etc., which may have been matched erroneously.
Provide only the terms that are truly relevant to the content.
Do not extract words from the text yourself, instead only pass the words given in the keywords.
Provide the response in JSON format.
Please use double quotes (") instead of single quotes (') to comply with JSON rules.
Must provide the response in JSON format without wrapping it in an "Output" field. Instead, return it directly in the format shown in the example response


Example Input:
{{
"text": "규정에 따른 갱신 거부는 허가 소지자 또는 다른 신청자가 갱신 거부에서 지적된 결함을 시정하기 위해 부지 또는 부지 사용 방법의 변경을 제안하는 새로운 신청서를 제출하는 것을 제한하지 않는다.",
"keywords": ['renewal - 갱신', 'provisions - 조항', 'permit - 허가', 'applicant - 지원자', 'site - 현장', 'deficiencies - 결점', 'denial - 거부', 'changes - 변경', 'filing - 제출', 'renewal - 갱신']
}}

Example response:
{{"keywords": ['renewal - 갱신', 'provisions - 조항', 'permit - 허가', 'applicant - 지원자', 'site - 현장', 'deficiencies - 결점', 'denial - 거부', 'changes - 변경', 'filing - 제출']}}


Input:
{{
"text": "{korean_text}",
"keywords": {keywords}
}}
""",
)
