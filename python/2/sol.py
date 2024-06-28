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
        return self.val == other.val and (self.next == other.next)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sourcery skip: assign-if-exp, reintroduce-else
        
        def add(l1: Optional[ListNode], l2: Optional[ListNode], carry: bool) -> Optional[ListNode]:
            if l1 is None and l2 is None:
                return None
            
            if l1 is None:
                if not carry:
                    return l2
                return add(l2, ListNode(1, None), False)
            
            if l2 is None:
                if not carry:
                    return l1
                return add(l1, ListNode(1, None), False)
            
            # l1 is not None, l2 is not None
            raw_value = l1.val + l2.val + carry
            new_value = raw_value % 10
            new_carry = raw_value // 10
            
            if l1.next is None and l2.next is None and new_carry:
                return ListNode(new_value, ListNode(1, None))
            
            return ListNode(new_value, add(l1.next, l2.next, new_carry))
        
        return add(l1, l2, False)