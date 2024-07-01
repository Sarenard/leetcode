from sol import Solution, ListNode

class Test:
    def run():  # sourcery skip: none-compare
        solution = Solution()
        assert solution.removeNthFromEnd(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2
        ) == ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
        assert solution.removeNthFromEnd(ListNode(1, None), 1) == None
        assert solution.removeNthFromEnd(ListNode(1, ListNode(2, None)), 1) == ListNode(1, None)
        

Test.run()
