from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.uniquePaths(3, 7) == 28
        assert solution.uniquePaths(3, 2) == 3

Test.run()
