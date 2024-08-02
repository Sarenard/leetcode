from typing import List, Optional
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]
        if nums.count(0) == 1:
            product = 1
            for num in nums:
                if num != 0:
                    product *= num
            return [0 if num != 0 else product for num in nums]
        product = 1
        for num in nums:
            product *= num
        result = []
        for num in nums:
            result.append(product // num)
        return result