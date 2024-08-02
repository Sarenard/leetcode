from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]
        assert solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

Test.run()
