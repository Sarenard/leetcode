from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.jump([2,3,1,1,4]) == 2
        assert solution.jump([2,3,0,1,4]) == 2
        assert solution.jump([2, 1]) == 1
        assert solution.jump([1,2,3]) == 2

Test.run()
