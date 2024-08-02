from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def get_length(start, nums):
            tested = set()
            length = 1
            while start+1 in nums:
                tested.add(start)
                start += 1
                length += 1
            return length, tested
        total = 0
        tested = set()
        nums.sort()
        for num in nums:
            if num in tested:
                continue
            new, testedn =get_length(num, nums)
            total = max(total, new)
            tested = tested.union(testedn)
        return total