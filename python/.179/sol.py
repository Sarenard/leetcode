from typing import List

class Number:
    def __init__(self, nb):
        self.nb = nb

    def __gt__(self, other):
        nb = str(self.nb)
        othernb = str(other.nb)
        if len(nb) == 1 and len(othernb) == 1:
            return self.nb < other.nb
        if nb[0] != othernb[0]:
            return int(nb[0]) < int(othernb[0])
        same = 0
        try:
            while nb[same] == othernb[same]:
                same += 1
        except Exception:
            pass
        if len(nb) == len(othernb):
            return Number(int(nb[same:])).__gt__(Number(int(othernb[same:])))
        return (
            Number(int(nb[same:])).__gt__(Number(int(othernb[same-1:])))
            if len(nb) > len(othernb)
            else Number(int(nb[same-1:])).__gt__(Number(int(othernb[same:])))
        )

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        mynums = [Number(x) for x in nums]
        mynums.sort()
        mynums2 = [str(nbr.nb) for nbr in mynums]
        return "".join(mynums2)