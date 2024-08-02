from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.climbStairs(2) == 2
        assert solution.climbStairs(3) == 3

Test.run()
