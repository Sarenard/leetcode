from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nb1str:str = ""
        while l1:
            nb1str = str(l1.val) + nb1str
            l1 = l1.next
        nb2str:str = ""
        while l2:
            nb2str = str(l2.val) + nb2str
            l2 = l2.next
        total:int = int(nb1str) + int(nb2str)
        totalstr:str = str(total)
        new_list:Optional[ListNode] = None
        for i in range(len(totalstr)):
            new_list = ListNode(int(totalstr[i]), new_list)
        return new_list


liste1:ListNode = ListNode(5, ListNode(6))
liste2:ListNode = ListNode(5, ListNode(4, ListNode(9)))

print(Solution().addTwoNumbers(liste1, liste2))