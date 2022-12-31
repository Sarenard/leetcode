class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need to do it a bit optimised
        # we need to use a sliding window
        # we need to keep track of the last index of each letter
        # we need to update the start of the window if we find a letter that was already seen
        # we need to update the max length
        # we need to return the max length
        max_length:int = 0
        start:int = 0
        last_seen:dict = {}
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= start:
                start = last_seen[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            last_seen[s[i]] = i
        return max_length