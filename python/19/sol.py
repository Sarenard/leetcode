from typing import List, Optional

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sourcery skip: assign-if-exp, reintroduce-else
        length = 0
        cur_head = head
        while cur_head:
            cur_head = cur_head.next
            length += 1
        def remove(tete, k):
            if k == 0:
                return tete.next
            return ListNode(tete.val, remove(tete.next, k-1))
        a = remove(head, length-n)
        return a