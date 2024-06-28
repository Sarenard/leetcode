from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 43
        assert solution.maximumImportance(5, [[0,3],[2,4],[1,3]]) == 20

Test.run()
