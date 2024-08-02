from typing import List, Optional
import math

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        total = 0
        while total < len(citations) and citations[len(citations) - total - 1] > total:
            total += 1
        return total