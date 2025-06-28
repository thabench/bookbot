def get_num_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str: int]:
    chars_count_dict = {}
    for char in text:
        char = char.lower()
        if not chars_count_dict.get(char):
            chars_count_dict[char] = 1
        else:
            chars_count_dict[char] += 1
    return chars_count_dict


def sort_on(char_dict: dict[str, int]) -> int:
    return char_dict["num"]


def sort_chars(char_dict: dict[str, int]) -> list[dict[str, str | int]]:
    char_list = list()
    for k, v in char_dict.items():
        if not k.isalpha():
            continue
        char_list.append({"char": k, "num": v})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
