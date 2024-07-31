from sol import Solution, ListNode

class Test:
    def run():
        solution = Solution()
        assert solution.mergeNodes(
            ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0, None))))))))
        ) == ListNode(4, ListNode(11, None))
        assert solution.mergeNodes(
            ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(5, ListNode(2, ListNode(2, ListNode(0, None)))))))))
        ) == ListNode(1, ListNode(3, ListNode(9, None)))

Test.run()
