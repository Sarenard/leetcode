class Solution:
    def numberOfSteps(self, num: int) -> int:
        total:int = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            total += 1
        return total