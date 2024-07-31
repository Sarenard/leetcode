from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
        assert solution.intersect([4,9,5], [9,4,9,8,4]) == [4, 9]

Test.run()
