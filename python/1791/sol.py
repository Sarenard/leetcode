from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1, edge2 = set(edges[0]), set(edges[1])
        return edge1.intersection(edge2).pop()