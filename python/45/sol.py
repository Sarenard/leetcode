from typing import List
from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length == 1:
            return 0
        
        global MAXI
        MAXI = float("inf")
    
        @lru_cache
        def canjump_bruteforce(current_index: int, current_nb: int) -> bool:
            buffer = []
            for saut in list(range(nums[current_index]+1))[::-1]:
                new_index = saut + current_index
                
                if new_index >= nums_length:
                    continue
                
                if new_index == nums_length-1:
                    return (current_nb+1, True)
                
                if new_index != current_index:
                    result = canjump_bruteforce(new_index, current_nb+1)
                    if result[1]:
                        return result
                    buffer.append(result[0])
                    
            return (min(buffer) if buffer else float("inf"), False)
        
        @lru_cache
        def canjump_limited(current_index: int, current_nb: int, MAXI: int) -> bool:
            if current_nb >= MAXI:
                return current_nb
            buffer = []
            for saut in list(range(nums[current_index]+1))[::-1]:
                new_index = saut + current_index
                
                if new_index >= nums_length:
                    continue
                
                if new_index == nums_length-1:
                    return current_nb+1
                
                if new_index != current_index:
                    result = canjump_limited(new_index, current_nb+1, MAXI)
                    buffer.append(result)
                    
            return min(buffer) if buffer else float("inf")
        
        result = canjump_bruteforce(0, 0)
        MAXI = result[0]
        new_result = canjump_limited(0, 0, MAXI)
            
        return new_result