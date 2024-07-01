from sol import Solution, TreeNode

class Test:
    def run():
        solution = Solution()
        assert solution.maxPathSum(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))) == 6
        assert solution.maxPathSum(TreeNode(-10, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))) == 42
        assert solution.maxPathSum(["2","1","+","3","*"]) == 9
        assert solution.maxPathSum(["2","1","+","3","*"]) == 9

Test.run()
