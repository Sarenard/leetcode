from sol import Solution, ListNode

class Test:
    def run():  # sourcery skip: none-compare
        solution = Solution()
        assert solution.mergeKLists(
            [
                ListNode(1, ListNode(4, ListNode(5, None))),
                ListNode(1, ListNode(3, ListNode(4, None))),
                ListNode(2, ListNode(6, None)),
            ]
        ) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6, None))))))))
        assert solution.mergeKLists([]) == None
        assert solution.mergeKLists([None]) == None
        

Test.run()
