from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.numWays("1001") == 0
        assert solution.numWays("0000") == 3
        assert solution.numWays("10101") == 4

Test.run()
