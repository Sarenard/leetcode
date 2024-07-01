from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.threeConsecutiveOdds([2,6,4,1]) == False
        assert solution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]) == True

Test.run()
