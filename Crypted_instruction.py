import string

DIGITS = set(string.digits)


def decode(encoded_string: str) -> str:
    """
    Декодирует строку, сжатую методом RLE с вложенностью.
    Формат: число[подстрока] — подстрока повторяется указанное число раз.
    Пример: '3[a2[b]]' → 'abbabbabb'
    """
    stack: list[tuple[str, int]] = []
    current: str = ""
    repeat_count: str = ""

    for char in encoded_string:
        if char in DIGITS:
            repeat_count += char
        elif char == "[":
            stack.append((current, int(repeat_count)))
            current = ""
            repeat_count = ""
        elif char == "]":
            prev_string, repeater = stack.pop()
            current = prev_string + current * repeater
        else:
            current += char

    return current


if __name__ == "__main__":
    line: str = input()
    print(decode(line))