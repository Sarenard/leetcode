from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            match x:
                case '(':
                    stack.append(')')
                case '[':
                    stack.append(']')
                case '{':
                    stack.append('}')
                case char:
                    if not stack:
                        return False
                    if stack.pop() != char:
                        return False
        return (not stack)