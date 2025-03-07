class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for value in s:
            if value in ('(','{','['):
                stack.append(value)
            elif value == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif value == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif value == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False

        if len(stack) != 0:
            return False
        return True
