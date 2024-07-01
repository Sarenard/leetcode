from sol import Solution, TreeNode

class Test:
    def run():
        solution = Solution()
        assert solution.isValidBST(
            TreeNode(2, None, None)
        ) == True
        assert solution.isValidBST(
            TreeNode(2, TreeNode(1,None, None), TreeNode(3, None, None))
        ) == True
        assert solution.isValidBST(
            TreeNode(5, TreeNode(1,None, None), TreeNode(4, TreeNode(3,None, None), TreeNode(6, None, None)))
        ) == False

Test.run()
