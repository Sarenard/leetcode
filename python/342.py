class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0 and bin(n).count('1') == 1) and (n & 0x55555555) == n