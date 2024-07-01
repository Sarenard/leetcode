from sol import Solution, ListNode

class Test:
    def run():  # sourcery skip: none-compare
        solution = Solution()
        assert solution.swapPairs(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        ) == ListNode(2, ListNode(1, ListNode(4, ListNode(3, None))))
        assert solution.swapPairs(None) == None
        assert solution.swapPairs(ListNode(1, None)) == ListNode(1, None)
        

Test.run()
