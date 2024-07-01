from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
        assert solution.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
        assert solution.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]) == 0

Test.run()
