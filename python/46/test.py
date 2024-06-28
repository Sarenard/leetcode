from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert solution.permute([0,1]) == [[0,1],[1,0]]
        assert solution.permute([1]) == [[1]]

Test.run()
