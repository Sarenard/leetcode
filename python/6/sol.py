from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lignes = [[] for _ in range(numRows)]
        total = 0
        i = 0
        reverse = False
        while total < len(s):
            lignes[i].append(s[total])
            # update i
            i += (-1 if reverse else 1)
            if i in [0, numRows-1]:
                reverse = not reverse
            total += 1
        words = ["".join(ligne) for ligne in lignes]
        return "".join(words)