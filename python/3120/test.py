from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.numberOfSpecialChars("aaAbcBC") == 3
        assert solution.numberOfSpecialChars("abc") == 0
        assert solution.numberOfSpecialChars("abBCab") == 1

Test.run()
