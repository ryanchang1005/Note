"""
Valid Parentheses
驗證括號

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""


def run(s):
    stack = []
    for ch in s:
        if ch in ['(', '[', '{']:
            stack.insert(0, ch)
        else:
            if len(stack) == 0:
                return False

            val = stack.pop(0)

            if ch == ')' and val == '(':
                continue
            elif ch == ']' and val == '[':
                continue
            elif ch == '}' and val == '{':
                continue
            else:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    print(run("()"))  # True
    print(run("()[]{}"))  # True
    print(run("(]"))  # False
    print(run("([)]"))  # False
    print(run("{[]}"))  # True
