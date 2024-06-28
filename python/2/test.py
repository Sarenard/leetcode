from sol import Solution, ListNode

class Test:
    def run():
        solution = Solution()
        assert solution.addTwoNumbers(
            (ListNode(2, ListNode(4, ListNode(3, None)))),
            (ListNode(5, ListNode(6, ListNode(4, None))))
        ) == ListNode(7, ListNode(0, ListNode(8, None)))
        assert solution.addTwoNumbers(
            (ListNode(5, None)),
            (ListNode(5, None))
        ) == ListNode(0, ListNode(1, None))

Test.run()
