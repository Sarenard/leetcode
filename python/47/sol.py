from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        sol = []
        myset = list(set(nums))
        for i in myset:
            # print(i, nums)
            newnums = nums.copy()
            newnums.pop(newnums.index(i))
            permuted = self.permuteUnique(newnums)
            for j in permuted:
                sol.append([i, *j])
        return sol
