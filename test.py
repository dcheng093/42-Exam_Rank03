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
    if i < len(s) and s[i] in "-+":
        sign = -1 if s[i] == '-' else 1; i += 1
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i]); i += 1
    return res * sign


def brackets(s: str) -> bool:
    stack, pairs = [], {"}": "{", "]": "[", ")": "("}
    for char in s:
        if char in "[{(":
            stack.append(char)
        elif char in "}])":
            if not stack or pairs[char] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0


def capitalize_words(s: str) -> str:
    words = s.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def convert_base(number: str, from_base: int, to_base: int) -> None:
    digits, res = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""
    try:
        if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
            print("ERROR"); return
        digit = int(number, from_base)
    except ValueError:
        print("ERROR"); return
    if digit == 0:
        print("0"); return
    while digit > 0:
        res = res + digits[digit % to_base]; digit //= to_base
    print(res[::-1])


def custom_sort(arr: list) -> list:
    res = arr[:]
    for i in range(len(res)):
        for j in range(0, len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


def merge_and_sort_desc(list1: list[int], list2: list[int]) -> list[int]:
    merged = list1 + list2; merged.sort(reverse=True); return merged


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]


def mirror_matrix_vertical(matrix: list) -> list:
    return matrix[::-1]


def py_echo_validator(s: str) -> bool:
    filtered = "".join(word.lower() for word in s if word.isalnum())
    return filtered[::-1] == filtered


def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if (text[i].isdigit() and
                text[i + 1].isdigit() and
                int(text[i + 1]) == int(text[i]) + 1):
            count += 1
    return count




def twoSum(nums: list[int], target: int) -> list[int]:
    seen: dict = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return []


def valid_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print("alternate case\n")
print(alternate_case("hello world"))              # "HeLlO wOrLd"
print(alternate_case("42madrid"))                 # "42MaDrId"
print(alternate_case("python3.9 rocks!"))         # "PyThOn3.9 RoCkS!"
print(alternate_case("a!b?c"))                    # "A!b?C"
print("\natoi\n")
print(atoi("42"))                                 # 42
print(atoi("  -42ab"))                            # -42
print(atoi("+123"))                               # 123
print(atoi("abc"))                                # 0
print("\nbrackets\n")
print(brackets("()"))                             # True
print(brackets("([{}])"))                         # True
print(brackets("(]"))                             # False
print(brackets("([)"))                            # False
print(brackets("a(b[c]d)"))                       # True
print(brackets("[{adaudna}]"))                    # True
print(brackets("[{adaudna}])"))                   # False
print(brackets("abc{[123(xyz)]}"))                # True
print("\ncapitalize_words\n")
print(capitalize_words("hello world"))            # "Hello World"
print(capitalize_words("42 madrid exam"))         # "42 Madrid Exam"
print(capitalize_words("  multiple   spaces "))   # "  Multiple   Spaces "
print(capitalize_words("mixed CASE letters"))     # "Mixed Case Letters"
print("\nconvert_base\n")
convert_base("ff", 16, 2)                         # 11111111
convert_base("10", 2, 10)                         # 2
convert_base("z", 36, 10)                         # 35
convert_base("1g", 16, 10)                        # ERROR
print("\ncustomSortString\n")
print(custom_sort([3, 1, 2]))                     # [1, 2, 3]
print(custom_sort([5, -1, 0]))                    # [-1, 0, 5])
print("\nmerge_and_sort_desc\n")
print(merge_and_sort_desc([1, 3, 5], [2, 4, 6]))  # [6, 5, 4, 3, 2, 1]
print(merge_and_sort_desc([10, 2], [3, 7, 2]))    # [10, 7, 3, 2, 2]
print(merge_and_sort_desc([], [1, 2, 3]))         # [3, 2, 1]
print(merge_and_sort_desc([], []))                # []
print("\nmirror_matrix\n")
res = mirror_matrix([
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]
                             ])
print("[")
for i, row in enumerate(res):
    comma = "," if i < len(res) - 1 else ""
    print(f"  {row}{comma}")
print("]")
print("\nmirror_matrix_vertical\n")
res = mirror_matrix_vertical([
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]
                             ])
print("[")
for i, row in enumerate(res):
    comma = "," if i < len(res) - 1 else ""
    print(f"  {row}{comma}")
print("]")
print("\npy_echo_validator\n")
print(py_echo_validator("Was it a car or a cat I saw?"))    # True
print(py_echo_validator("tab a cat"))                       # False
print(py_echo_validator("A man, a plan, a canal: Panama"))  # True
print(py_echo_validator("No lemon, no melon"))              # True
print("\npy_pattern_tracker\n")
print(pattern_tracker("12a34"))   # 2
print(pattern_tracker("1234"))    # 3
print(pattern_tracker("a1b2c3"))  # 0
print(pattern_tracker("98"))      # 0
print("\nsorted\n")
# sort strings by length
words = ["banana", "kiwi", "fig"]
result = sorted(words, key=lambda x: len(x))
print(result)
# sort tuples by a specific field
people = [("Ana", 8.5), ("Luis", 6.0)]
result = sorted(people, key=lambda x: x[1], reverse=True)
print(result)
# sort by multiple criteria
people = [("Ana", 20), ("Luis", 20), ("Marta", 18)]
result = sorted(people, key=lambda x: (x[1], x[0]))
print("\ntwoSum\n")
print(twoSum([2, 7, 11, 15], 9))                  # [0, 1]
print(twoSum([5, 5], 10))                         # [0, 1]
print("\nvalid_anagram\n")
print(valid_anagram("racecar", "carrace"))        # True
print(valid_anagram("jar", "jam"))                # False
print(valid_anagram("listen", "silent"))          # True
print(valid_anagram("aabbcc", "abcabc"))          # True
print(valid_anagram("abc", "ab"))                 # False
