from typing import List, Optional
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = prices[::-1]
        maxi_window = [0 for _ in range(len(prices))]
        maxi_window[0] = prices[0]
        for i, item in enumerate(prices[1:]):
            maxi_window[i+1] = max(maxi_window[i], item)
        prices = prices[::-1]
        maxi_window = maxi_window[::-1]
        best = 0
        for i, item in enumerate(prices):
            best = max(best, maxi_window[i] - item)
        return best