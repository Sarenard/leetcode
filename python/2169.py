class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        nb:int = 0
        while num1 * num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            nb += 1
        return nb