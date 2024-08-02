from typing import List

from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mydeque = deque(nums)
        mydeque.rotate(k)
        for i in range(len(nums)):
            nums[i] = mydeque[i]