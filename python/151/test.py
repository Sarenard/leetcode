from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.reverseWords("the sky is blue") == "blue is sky the"
        assert solution.reverseWords("  hello world  ") == "world hello"
        assert solution.reverseWords("a good   example") == "example good a"

Test.run()
