from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # numb = n + n+1 + n+2
        # numb = 3n + 3
        # numb = 3(n+1)
        if num % 3 != 0:
            return []
        res = num // 3
        return [res-1, res, res+1]