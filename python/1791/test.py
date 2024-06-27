from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.findCenter([[1,2],[2,3],[4,2]]) == 2
        assert solution.findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1

Test.run()
