# we can use recursion to solve this problem
# but we need to add a cache to avoid duplicate calculation
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)