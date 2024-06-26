from typing import List

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1:
            return True
        while True:
            if n % 2 == 0:
                n = n // 2
                continue
            if n % 3 == 0:
                n = n // 3
                continue
            if n % 5 == 0:
                n = n // 5
                continue
            break
        return n == 1