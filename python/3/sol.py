from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        match len(s):
            case 0:
                return 0
            case 1:
                return 1
        i, j = 0, 0
        letters = {s[0]}
        maxl = 0
        while j != len(s) - 1:
            if s[j+1] in letters:
                letters.remove(s[i])
                i += 1
            else:
                j += 1
                letters.add(s[j])
            if j - i + 1 > maxl:
                maxl = j-i+1
        return maxl