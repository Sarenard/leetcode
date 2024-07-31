from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicopresence1 = {
            k:0 for k in [*nums1, *nums2]
        }
        for k in nums1:
            dicopresence1[k] += 1
        dicopresence2 = {
            k:0 for k in [*nums1, *nums2]
        }
        for k in nums2:
            dicopresence2[k] += 1
        dicoresult = {
            k:min(dicopresence1[k], dicopresence2[k]) for k in [*nums1, *nums2]
        }
        result = []
        for k, i in dicoresult.items():
            result.extend([k]*i)
        return result