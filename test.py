def alternate_case(s: str) -> str:
    res, count = "", 0
    for char in s:
        if char.isalpha():
            if count % 2 == 0:
                res += char.upper()
            else:
                res += char.lower()
            count += 1
        else:
            res += char
    return res


def atoi(s: str) -> int:
    s, i, res, sign = s.strip(), 0, 0, 1
    if i < len(s) and s[i] in '-+':
        sign = 1 if s[i] == '+' else -1; i += 1
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i]); i += 1
    return (res * sign)


def brackets(s: str) -> bool:
    stack, pairs = [], {'}': '{', ']': '[', ')': '('}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in '}])':
            if not stack or pairs[char] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0


def capitalize_words(s: str) -> str:
    words = s.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


print("alternate case\n")
print(alternate_case("hello world"))             # "HeLlO wOrLd"
print(alternate_case("42madrid"))                # "42MaDrId"
print(alternate_case("python3.9 rocks!"))        # "PyThOn3.9 RoCkS!"
print(alternate_case("a!b?c"))                   # "A!b?C"
print("\natoi\n")
print(atoi("42"))                                # 42
print(atoi("  -42ab"))                           # -42
print(atoi("+123"))                              # 123
print(atoi("abc"))                               # 0
print("\nbrackets\n")
print(brackets("()"))                            # True
print(brackets("([{}])"))                        # True
print(brackets("(]"))                            # False
print(brackets("([)"))                           # False
print(brackets("a(b[c]d)"))                      # True
print(brackets("[{adaudna}]"))                   # True
print(brackets("[{adaudna}])"))                  # False
print(brackets("abc{[123(xyz)]}"))               # True
print("\ncapitalize_words\n")
print(capitalize_words("hello world"))           # "Hello World"
print(capitalize_words("42 madrid exam"))        # "42 Madrid Exam"
print(capitalize_words("  multiple   spaces "))  # "  Multiple   Spaces "
print(capitalize_words("mixed CASE letters"))    # "Mixed Case Letters"
