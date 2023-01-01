class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x:int = int(dividend / divisor)
        if x > 2147483647:
            return 2147483647
        elif x < -2147483648:
            return -2147483648
        return x