from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.maxProfit([7,1,5,3,6,4]) == 7
        assert solution.maxProfit([1,2,3,4,5]) == 4
        assert solution.maxProfit([7,6,4,3,1]) == 0

Test.run()
