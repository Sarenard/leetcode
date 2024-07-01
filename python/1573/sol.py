from typing import List
from math import comb

class Solution:
    def numWays(self, s: str) -> int:
        nb = s.count("1")
        if nb % 3 != 0:
            return 0
        
        if nb == 0:
            return comb(len(s)-1, 2) % (10 ** 9 + 7)
        
        number = nb // 3
        
        start1 = 0
        
        i = 0
        total = 0
        while total < number:
            if s[i] == "1":
                total += 1
            i += 1
        end1 = i
        
        while s[i] != "1":
            i += 1
        start2 = i
        
        total = 0
        while total < number:
            if s[i] == "1":
                total += 1
            i += 1
        end2 = i
        
        while s[i] != "1":
            i += 1
        start3 = i
        
        end3 = len(s)-1

        nb_combi_1 = start2-end1+1
        nb_combi_2 = start3-end2+1
        
        total = nb_combi_1 * nb_combi_2

        return (total % (10 ** 9 + 7))