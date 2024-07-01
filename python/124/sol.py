from typing import List, Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we build the graph
        adjgraph = {}
        def build(arbre):
            if arbre is None:
                return
            if arbre.left is not None:
                try:
                    adjgraph[arbre.val].add(arbre.left.val)
                except Exception:
                    adjgraph[arbre.val] = {arbre.left.val}
                try:
                    adjgraph[arbre.left.val].add(arbre.val)
                except Exception:
                    adjgraph[arbre.left.val] = {arbre.val}
                build(arbre.left)
            if arbre.right is not None:
                try:
                    adjgraph[arbre.val].add(arbre.right.val)
                except Exception:
                    adjgraph[arbre.val] = {arbre.right.val}
                try:
                    adjgraph[arbre.right.val].add(arbre.val)
                except Exception:
                    adjgraph[arbre.right.val] = {arbre.val}
                build(arbre.right)
        build(root)
        print(adjgraph)