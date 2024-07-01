from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.countOrders(1) == 1
        assert solution.countOrders(2) == 6
        assert solution.countOrders(3) == 90

Test.run()
