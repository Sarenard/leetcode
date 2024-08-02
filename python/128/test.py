from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.longestConsecutive([100,4,200,1,3,2]) == 4
        assert solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

Test.run()
