def brackets(s: str) -> bool:
    stack, pairs = [], {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')}]':
            if not stack or pairs[char] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0


print(brackets("()"))
print(brackets("([{}])"))
print(brackets("(]"))
