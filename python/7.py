class Solution:
    def reverse(self, x: int) -> int:
        # we need to reverse the number
        y:int = str(x) if x >= 0 else str(x)[1:]
        y = y[::-1]
        y = int(y) if x >= 0 else -int(y)
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y
