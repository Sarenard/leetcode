from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.maxProfit([7,1,5,3,6,4]) == 5
        assert solution.maxProfit([7,6,4,3,1]) == 0

Test.run()
