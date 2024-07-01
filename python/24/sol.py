from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    
    def __eq__(self, other):
        return self.next == other.next and self.val == other.val
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ListNode.__match_args__ = ("val", "next") 
        match head:
            case None:
                return None
            case ListNode(val, None):
                return ListNode(val, None)
            case ListNode(val1, ListNode(val2, thing)):
                return ListNode(val2, ListNode(val1, self.swapPairs(thing)))