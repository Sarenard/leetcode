from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def keys(tree: TreeNode):
    if tree is None:
        return []
    total = [tree.val]
    total.extend(keys(tree.left))
    total.extend(keys(tree.right))
    return total

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (
            all(x < root.val for x in keys(root.left))
            and all(x > root.val for x in keys(root.right))
            and self.isValidBST(root.left)
            and self.isValidBST(root.right)
        )