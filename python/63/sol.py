from typing import List

from functools import lru_cache

from sys import setrecursionlimit
setrecursionlimit(1_000_000_000)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache
        def uniquePaths(m: int, n: int) -> int:
            # sourcery skip: assign-if-exp, reintroduce-else
            if obstacleGrid[m-1][n-1]:
                return 0
            if n == 1 and m == 1:
                return 1
            if n == 1:
                return uniquePaths(m-1, 1)
            if m == 1:
                return uniquePaths(1, n-1)
            return uniquePaths(m-1, n)+uniquePaths(m, n-1)
        if obstacleGrid[0][0]:
            return 0
        return uniquePaths(len(obstacleGrid), len(obstacleGrid[0]))