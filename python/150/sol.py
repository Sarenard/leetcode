from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(math.trunc(b / a))
                case nb:
                    stack.append(int(nb))
        return stack.pop()