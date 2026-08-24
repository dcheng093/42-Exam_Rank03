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


# Non-alphabetic characters are preserved
# and do not affect the alternation.

# The examples in the subject appear to be inconsistent
# with this rule.
print(alternate_case("hello world"))  # "HeLlO wOrLd"
print(alternate_case("42madrid"))  # "42MaDrId"
print(alternate_case("python3.9 rocks!"))  # "PyThOn3.9 RoCkS!"
print(alternate_case("a!b?c"))  # "A!b?C"
