from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.firstMissingPositive([3,-1,4,-1,1]) == 2
        assert solution.firstMissingPositive([1,2,0]) == 3
        assert solution.firstMissingPositive([7,8,9,11,12]) == 1
        assert solution.firstMissingPositive([1]) == 2
        assert solution.firstMissingPositive([2, 1]) == 3

Test.run()
