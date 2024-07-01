from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.numTrees(3) == 5
        assert solution.numTrees(1) == 1

Test.run()
