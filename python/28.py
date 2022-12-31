class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while len(needle) <= len(haystack):
            if haystack[:len(needle)] == needle:
                return index
            haystack = haystack[1:]
            index += 1
        return -1
    
print(Solution().strStr("hello", "ll"))