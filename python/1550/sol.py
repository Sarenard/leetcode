from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        new = list(map(lambda x : x % 2, arr))
        new2 = map(lambda x: sum(new[i] for i in [x, x+1, x+2]), range(len(arr)-2))
        return 3 in new2