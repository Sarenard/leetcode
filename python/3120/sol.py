from typing import List

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # sourcery skip: inline-immediately-returned-variable, move-assign-in-block, sum-comprehension
        letters = set(map(ord, word))
        total = 0
        diff = ord("a")-ord("A")
        for i in range(ord("A"), ord("Z")+1):
            if i in letters and i + diff in letters:
                total += 1
        return total