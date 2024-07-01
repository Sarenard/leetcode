from typing import List, Optional

from functools import lru_cache

class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        if n in [0, 1]:
            return 1
        total = 0
        for i in range(0, n): # [[0; n-1]]
            total += self.numTrees(i) * self.numTrees(n-1-i)
        return total