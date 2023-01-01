class Solution:
    def mySqrt(self, x: int) -> int:
        # don't use math.sqrt or ** 0.5
        # use binary search
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right