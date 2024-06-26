from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.isUgly(6) == True
        assert solution.isUgly(1) == True
        assert solution.isUgly(14) == False

Test.run()
