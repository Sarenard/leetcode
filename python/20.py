class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return len(stack) == 0