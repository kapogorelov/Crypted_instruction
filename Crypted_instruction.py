# ID посылки: 162458389

import string

DIGITS = set(string.digits)


def decode(encoded_string: str) -> str:
    stack: list[tuple[str, int]] = []
    current_segment: str = ""
    repeat_count: str = ""

    for char in encoded_string:
        if char in DIGITS:
            repeat_count += char
        elif char == "[":
            stack.append((current_segment, int(repeat_count)))
            current_segment = ""
            repeat_count = ""
        elif char == "]":
            preceding_segment, repeater = stack.pop()
            current_segment = preceding_segment + current_segment * repeater
        else:
            current_segment += char

    return current_segment


if __name__ == "__main__":
    line: str = input()
    print(decode(line))
