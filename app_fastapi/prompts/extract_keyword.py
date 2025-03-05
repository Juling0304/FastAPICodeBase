from langchain.prompts import PromptTemplate

cn_prompt = PromptTemplate(
    input_variables=["long_text"],
    template="""Extract keywords from the content of the input.
The criteria for extracting keywords are as follows:

1. Extract Taekwondo-related technical terms (e.g., flying kick, backhand, etc.)
2. Extract proper nouns (e.g., organization names, personal names, place names, textbook titles, etc.)
3. Extract table of contents and titles, sub title
4. Terms with Korean characters and English characters in parentheses
5. Terms within special symbols (e.g., <educational video>, 『Guanzi』, <Clementine>, (TigerJK), etc.)
6. Exclude dates (e.g., 1995, 1982, 2023-10-05, December 25, etc.).

Extract the keywords according to the above criteria.
Provide the response in JSON format.
The key should be the extracted Chinese keyword, and the value should be its corresponding translation in Korean.
The key should be Chinese

Example response:
{{"跆拳道": "태권도", "概念": "개념"}}


Input:
{long_text}
""",
)


ko_prompt = PromptTemplate(
    input_variables=["long_text"],
    template="""Extract Korean keywords from the content of the input.
The criteria for extracting keywords are as follows:

1. Extract Taekwondo-related technical terms (e.g., flying kick, backhand, etc.)
2. Extract proper nouns (e.g., organization names, personal names, place names, textbook titles, etc.)
3. Extract table of contents and titles, sub title
4. Terms with Korean characters and Chinese characters in parentheses (e.g., definition(定義), training(訓鍊, training), ‘修’, acculturation（文化接變）)
5. Terms within special symbols (e.g., <educational video>, 『Guanzi』, <Clementine>, (TigerJK), etc.)
6. Exclude dates (e.g., 1995, 1982, 2023-10-05, December 25, etc.).

Extract the keywords according to the above criteria.
Provide the response in JSON format.
The key should be the extracted Korean keyword, and the value should be its corresponding translation in Chinese.
The key should be Korean


Example response:
{{"태권도": "跆拳道", "개념": "概念"}}


Input:
{long_text}
""",
)


en_prompt = PromptTemplate(
    input_variables=["long_text"],
    template="""Extract English keywords from the content of the input.
The criteria for extracting keywords are as follows:

1. Extract Taekwondo-related technical terms (e.g., flying kick, backhand, etc.)
2. Extract proper nouns (e.g., organization names, personal names, place names, textbook titles, etc.)
3. Extract table of contents and titles, sub title
4. Terms with Korean characters and Chinese characters in parentheses (e.g., definition(定義), training(訓鍊, training), ‘修’, acculturation（文化接變）)
5. Terms within special symbols (e.g., <educational video>, 『Guanzi』, <Clementine>, (TigerJK), etc.)
6. Exclude dates (e.g., 1995, 1982, 2023-10-05, December 25, etc.).

Extract the keywords according to the above criteria.
Provide the response in JSON format.
The key should be the extracted English keyword, and the value should be its corresponding translation in Korean.
The key should be English


Example response:
{{"taekwondo": "태권도", "concept": "개념"}}


Input:
{long_text}
""",
)

ko_en_prompt = PromptTemplate(
    input_variables=["long_text"],
    template="""Extract Korean keywords from the content of the input.
The criteria for extracting keywords are as follows:

1. Extract Taekwondo-related technical terms (e.g., flying kick, backhand, etc.)
2. Extract proper nouns (e.g., organization names, personal names, place names, textbook titles, etc.)
3. Extract table of contents and titles, sub title
4. Terms with Korean characters and Chinese characters in parentheses (e.g., definition(定義), training(訓鍊, training), ‘修’, acculturation（文化接變）)
5. Terms within special symbols (e.g., <educational video>, 『Guanzi』, <Clementine>, (TigerJK), etc.)
6. Exclude dates (e.g., 1995, 1982, 2023-10-05, December 25, etc.).

Extract the keywords according to the above criteria.
Provide the response in JSON format.
The key should be the extracted Korean keyword, and the value should be its corresponding translation in English.
The key should be Korean


Example response:
{{"태권도": "taekwondo", "개념": "concept"}}


Input:
{long_text}
""",
)
