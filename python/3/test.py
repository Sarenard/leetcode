from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.lengthOfLongestSubstring("abcabcbb") == 3
        assert solution.lengthOfLongestSubstring("bbbb") == 1
        assert solution.lengthOfLongestSubstring("pwwkew") == 3

Test.run()
