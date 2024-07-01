from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j, item in enumerate(nums):
            if item == val:
                continue
            else:
                nums[i] = nums[j]
                i += 1
        return i