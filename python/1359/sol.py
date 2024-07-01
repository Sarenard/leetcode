from typing import List

from functools import lru_cache

class Solution:
    @lru_cache
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        other = self.countOrders(n-1)
        total = other * 2 * n * 2 * n - (2*n*(2*n-1)//2) * other - other * 2 * n
        return total % (10**9 + 7)