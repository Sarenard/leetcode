from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.hIndex([3,0,6,1,5]) == 3
        assert solution.hIndex([1,3,1]) == 1

Test.run()
