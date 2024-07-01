from sol import Solution, ListNode

class Test:
    def run():
        solution = Solution()
        assert solution.insertGreatestCommonDivisors(
            ListNode(18, ListNode(6, ListNode(10, ListNode(3, None))))
        ) == ListNode(18, ListNode(6, ListNode(6, ListNode(2, ListNode(10, ListNode(1, ListNode(3, None)))))))

Test.run()
