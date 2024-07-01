from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.permuteUnique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]]
        assert solution.permuteUnique([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert solution.permuteUnique([1]) == [[1]]

Test.run()
