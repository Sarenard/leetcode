from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    def __eq__(self, other):
        return self.next == other.next and self.val == other.val
        
def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b != 0:
        a,b=b,a%b
    return a

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ListNode.__match_args__ = ("val", "next") 
        match head:
            case None:
                return None
            case ListNode(val, None):
                return ListNode(val, None)
            case ListNode(val1, ListNode(val2, thing)):
                return ListNode(val1, ListNode(pgcd(val1, val2), self.insertGreatestCommonDivisors(ListNode(val2, thing))))