from typing import List, Optional

from functools import reduce

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.next == other.next and self.val == other.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        too_slow = """
        # if everything is None we return
        if all(liste is None for liste in lists):
            return None
        # on trouve les index
        indexes = [(liste.val if liste is not None else None) for liste in lists]
        i, val = -1, float("inf")
        for i2, val2 in enumerate(indexes):
            if val2 is None:
                continue
            if val2 < val:
                i, val = i2, val2
        lists = [(liste.next if j == i else liste) for j, liste in enumerate(lists)]
        return ListNode(val, self.mergeKLists(lists))
        """
        # we get all indices
        ListNode.__match_args__ = ("val", "next") 
        indices = []
        for liste in lists:
            while True:
                match liste:
                    case None:
                        break
                    case ListNode(val, suiv):
                        liste = suiv
                        indices.append(val)
        indices.sort(reverse = True)
        def construct():
            if indices:
                val = indices.pop()
                return ListNode(val, construct())
            return None
        return construct()