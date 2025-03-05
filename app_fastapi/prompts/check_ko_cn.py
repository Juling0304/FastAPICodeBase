from langchain.prompts import PromptTemplate

check_ko_cn_prompt_v1 = PromptTemplate(
    input_variables=["korean", "chinese", "keywords"],
    template="""
```task
    Korean->Chinese Taekwondo translation proofreading

```input_format
    {{"Korean" : "Source text (Korean)", "Chinese" : "Translation text (Chinese)", "keywords": "[Korean-Chinese pair keyword]"}}

```output_json_format
    {{"result": "Proofreading result (Corrected Chinese)", "errors":["Detected errors","Detected errors","Detected errors"]}}

Proofreading Guidelines 
    1. Basic Error Detection  
        Untranslated: If Korean characters (가-힣) remain → Tag as "Untranslated" 
        Ungrammatical: Detect sentences that don't follow Chinese grammar rules 
        Duplicate notations: 马步(马步) → Correct to 马步 
        Notation pattern: (\w+)(\1) → $1 

    2. Terminology Mistranslation Check  
        Compare with terminology glossary to detect mistranslations 
        One-to-one terminology comparison between source and translation 
        Correct mistranslations using the glossary 
        Key check patterns: Jab → 直权(直拳) → Correct to 刺拳 Straight → 刺权(刺拳) → Correct to 直拳 Taekkyeon → 태권/태권도/태권(跆拳/跆拳道/泰拳) → Correct to 跆跟 

    3. Terminology Consistency Check  
        Check consistency of Chinese translations for the same Korean terms 
        Detect terms that don't match standard translations in the glossary 
        Inconsistent terms → Correct using glossary 
        Ensure consistent translation terms throughout the document 

    4. Korean Pronunciation Processing Check  
        Check processing of Korean pronunciation emphasis words ("태깽이", "깽꺵이", etc.):  
        If meaning can be conveyed in Chinese → Use appropriate Chinese semantic translation 
        If meaning is difficult to convey:  
        If derived from Chinese characters → Use Chinese character (romanization) format 
        If not derived from Chinese characters → Use English romanization only 
        Example: "세니[L2] (Seni)" → Correct to "Seni" 

    5. Sentence Structure and Unnatural Expression Check  
        Detect repeated use of conjunctions (e.g., "因此") 
        Detect unnatural expressions:  
        Describing Taekwondo as "道路" 
        Inappropriate use of metaphors/similes 
        Culturally inappropriate expressions 
        Check subject-predicate agreement 
        Check expressions that don't match the context 

    6. Marking Rules  
        [NeedsConfirmation]: Items requiring confirmation 
        [Untranslated]: Untranslated parts 
        Check and correct unnecessary notations 

Execution Order 
    1. Check for untranslated/remaining Korean text 
    2. Check mistranslations against glossary 
    3. Check and correct terminology consistency 
    4. Check and correct Korean pronunciation processing 
    5. Check sentence structure and unnatural expressions 
    6. Check notation format 
    7. Make corrections using glossary 
    8. Output comprehensive results 

Must response format is JSON format
following output_json_format

```input
{{"Korean" : "{korean}", "Chinese" : "{chinese}", "keywords": {keywords}}}
""",
)


check_ko_cn_prompt_v2 = PromptTemplate(
    input_variables=["korean", "chinese", "keywords"],
    template="""
task: Korean->Chinese Taekwondo translation proofreading 

input_format: 

    {{"Korean": "Source text (Korean)", "Chinese": "Translation text (Chinese)", "keywords": ["Korean-Chinese pair keywords"]}} 

output_json_format: 

    {{"result": "Proofreading result (Corrected Chinese)", "errors": ["Error 1", "Error 2", "Error 3"]}} 

Proofreading Guidelines: 

1. Preservation First Principle 

   - Maintain original meaning as the highest priority 

   - When uncertain, preserve the existing translation 

   - Make minimal necessary changes only when there's a clear error 

2. Taekwondo Terminology Expertise 

   - Strictly follow specific terminology: 

Key check patterns: Jab → 直权(直拳) → Correct to 刺拳 Straight → 刺权(刺拳) → Correct to 直拳 Taekkyeon → 태권/태권도/태권(跆拳/跆拳道/泰拳) → Correct to 跆跟 

- Always correct parallel notation errors: 马步(马步) → 马步 

   - Notation pattern: (\w+)(\1) → $1 

   - Special attention terms: 

     - Jab → 刺拳 (not 直权) 

     - Straight → 直拳 (not 刺权) 

     - 무예(武艺) → generally more natural to translate as 武术 

   - Use the provided keyword glossary as reference, applying contextually 

3. Terminology Consistency Maintenance 

   - Check consistency of Chinese translations for the same Korean terms 

   - Ensure consistent translation terms throughout the document 

   - Detect and correct terms that don't match standard translations in the glossary 

4. Error Detection Hierarchy (in priority order) 

   a. Critical meaning errors (changes that alter technical instructions) 

   b. Parallel notation and formatting errors 

   c. Untranslated Korean text 

   d. Terminology inconsistency with established standards 

   e. Grammar and natural expression issues 

5. Korean Pronunciation Processing Check 

   - Check processing of Korean pronunciation emphasis words ("태깽이", "깽꺵이", etc.): 

     - If meaning can be conveyed in Chinese → Use appropriate Chinese semantic translation 

     - If meaning is difficult to convey: 

       - If derived from Chinese characters → Use Chinese character (romanization) format 

       - If not derived from Chinese characters → Use English romanization only 

     - Example: "세니[L2] (Seni)" → Correct to "Seni" 

6. Natural Chinese Expression 

   - Avoid mechanical word-for-word translations 

   - Check subject-predicate agreement 

   - Preserve specialized Taekwondo expressions but in natural Chinese 

   - Ensure cultural appropriateness while maintaining technical accuracy 

7. Context-Aware Correction 

   - Consider the entire sentence and surrounding context 

   - Preserve stylistic elements of the original where possible 

   - Only standardize terminology when it improves clarity 

8. Correction Restraint 

   - Avoid "hypercorrection" - don't change correct translations 

   - When multiple translations are acceptable, preserve the translator's choice 

   - Only substitute terms when there's a clear improvement in accuracy or clarity 

9. Marking Rules 

   - [NeedsConfirmation]: Items requiring confirmation 

   - [Untranslated]: Untranslated parts 

   - Check and correct unnecessary notations 

Execution Order 

1. Check for untranslated/remaining Korean text 

2. Check parallel notation errors and formatting 

3. Check mistranslations against glossary 

4. Check and correct terminology consistency 

5. Check and correct Korean pronunciation processing 

6. Check sentence structure and unnatural expressions 

7. Make final corrections using glossary 

8. Output comprehensive results 

Remember: The goal is to correct actual errors while respecting the translator's work. Favor minimal intervention and preserve meaning above all. 

The response must be in JSON format according to the output_json_format. 

input
{{"Korean" : "{korean}", "Chinese" : "{chinese}", "keywords": {keywords}}}
""",
)


check_ko_cn_prompt_v3 = PromptTemplate(
    input_variables=["korean", "chinese"],
    template="""
task: Korean->Chinese Taekwondo translation proofreading 

input_format: 

    {{"Korean": "Source text (Korean)", "Chinese": "Translation text (Chinese)", "keywords": ["Korean-Chinese pair keywords"]}} 

output_json_format: 

    {{"result": "Proofreading result (Corrected Chinese)", "errors": ["Error 1", "Error 2", "Error 3"]}} 


Proofreading rules: 

1. Check for untranslated text: Verify no Korean characters remain and ensure complete translation 

2. Fix notation errors: Correct redundant notations like 马步(马步) → 马步 

3. Improve sentence quality: 

- Use professional and formal expressions appropriate for Taekwondo textbooks 

- Improve to concise and clear sentence structures 

- Reflect the style of Chinese martial arts/sports textbooks 

- Remove unnecessary repetition or awkward expressions 

- Modify expressions to clearly convey educational content 

Error categories: 

- [UNTRANSLATED]: Korean text remaining in translation 

- [NOTATION]: Redundant or incorrect notation format 

- [STYLE]: Awkward phrasing that needs improvement while preserving meaning 

Work order: 

1. Check and correct untranslated text 

2. Fix notation errors 

3. Improve sentence quality (while maintaining exact meaning) 

input
{{"Korean" : "{korean}", "Chinese" : "{chinese}"}}
""",
)

check_ko_cn_prompt_v4 = PromptTemplate(
    input_variables=["korean", "chinese"],
    template="""
task: Korean->Chinese Taekwondo translation proofreading 

input_format: 

    {{"Korean": "Source text (Korean)", "Chinese": "Translation text (Chinese)"}} 

output_json_format: 

    {{"result": "Proofreading result (Corrected Chinese)", "errors": ["Error 1", "Error 2", "Error 3"]}} 


Proofreading rules: 

    1. Check for untranslated text: Verify no Korean characters remain and ensure complete translation 

    2. Fix notation errors: Correct redundant notations like 马步(马步) → 马步 

    3. Improve sentence quality:  

        - Maintain translator's original translations for Taekwondo terminology 

        - Improve only general sentences to match textbook style 

        - Improve to concise and clear sentence structures 

        - Remove unnecessary repetition or awkward expressions 

        - Modify expressions to clearly convey educational content 

Error Categories: 

    - [UNTRANSLATED]: Korean text remaining in translation 

    - [NOTATION]: Redundant or incorrect notation format 

    - [STYLE]: Awkward phrasing that needs improvement while preserving meaning 

Work Order: 

    1. Check and correct untranslated text 

    2. Fix notation errors 

    3. Improve sentence quality (while maintaining exact meaning) 

input
{{"Korean" : "{korean}", "Chinese" : "{chinese}"}}
""",
)
