# ID посылки: 162458389

def decode(s: str) -> str:
    str_stack: list[str] = []
    num_stack: list[int] = []
    current: str = ""
    num: str = ""

    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == "[":
            str_stack.append(current)
            num_stack.append(int(num))
            current = ""
            num = ""
        elif ch == "]":
            count: int = num_stack.pop()
            prev: str = str_stack.pop()
            current = prev + current * count
        else:
            current += ch

    return current


line: str = input()
print(decode(line))
