from typing import List, Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    def __eq__(self, other):
        return (other is not None) and self.next == other.next and self.val == other.val
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ListNode.__match_args__ = ("val", "next") 
        nouvelle_liste = None
        def suivant(head, nouvelle_liste):
            head = head.next
            total = 0
            while head.val != 0:
                total += head.val
                head = head.next
            return head, ListNode(total, nouvelle_liste)
        while head.next is not None:
            head, nouvelle_liste = suivant(head, nouvelle_liste)
            
        def reverse_list(liste):
            stack = []
            while liste is not None:
                stack.append(liste.val)
                liste = liste.next
            new = None
            i = 0
            while i < len(stack):
                new = ListNode(stack[i], new)
                i += 1
            return new
        
        liste = reverse_list(nouvelle_liste)
        
        print(nouvelle_liste)
        print(liste)
        
        return liste