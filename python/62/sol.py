from typing import List

from functools import lru_cache

class Solution:
    @lru_cache
    def uniquePaths(self, m: int, n: int) -> int:
        # sourcery skip: assign-if-exp, reintroduce-else
        if n == 1:
            return 1
        if m == 1:
            return 1
        return self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)