def is_text_completely_in_set(text: str, char_set: set) -> bool:
    # 주석 코드는 간단하지만 속도가 약 1/40 임
    # return all(character in char_set for character in text)
    result = True

    for character in text:
        if not character in char_set:
            result = False
            break

    return result
