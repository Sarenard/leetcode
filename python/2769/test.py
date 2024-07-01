from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.theMaximumAchievableX(4, 1) == 6
        assert solution.theMaximumAchievableX(3, 2) == 7

Test.run()
