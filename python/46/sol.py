from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        sol = []
        for i in nums:
            myset = set(nums)
            myset.remove(i)
            permuted = self.permute(list(myset))
            for j in permuted:
                sol.append([i, *j])
        return sol