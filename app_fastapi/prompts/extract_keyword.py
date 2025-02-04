from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["long_text"],
    template="""Extract keywords from the content of the input.
The criteria for extracting keywords are as follows:

1. Taekwondo-related technical terms (e.g., flying kick, backhand, etc.)
2. Proper nouns (e.g., organization names, personal names, place names, textbook titles, etc.)
3. Table of contents and titles
4. Terms with Korean characters and Chinese characters in parentheses (e.g., definition(定義), training(訓鍊, training), ‘修’, acculturation（文化接變）)
5. Terms within special symbols (e.g., <educational video>, 『Guanzi』, <Clementine>, (TigerJK), etc.)

Extract the keywords according to the above criteria.
Provide the response in JSON format.
The key should be the extracted Chinese keyword, and the value should be its corresponding translation in Korean.

Example response:
{{"跆拳道": "태권도", "概念": "개념"}}


Input:
{long_text}
""",
)
