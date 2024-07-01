from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.sumOfThree(33) == [10,11,12]
        assert solution.sumOfThree(4) == []

Test.run()
