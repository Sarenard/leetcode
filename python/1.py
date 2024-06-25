from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        presents = set(nums)
        if target % 2 == 0 and target // 2 in presents and len(list(filter(lambda x : x == target // 2, nums))) == 2:
            liste = [-1, -1]
            one = True
            for i in range(len(nums)):
                if nums[i] == target//2:
                    liste[one] = i
                    one = False
            return (liste[0], liste[1])
        for i in nums:
            presents.remove(i)
            if target-i in presents:
                return (nums.index(i), nums.index(target - i))
            presents.add(i)