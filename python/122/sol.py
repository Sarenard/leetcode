from typing import List, Optional
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        bought = False
        for i in range(len(prices)):
            # on achete de toute façon
            if not bought:
                total_profit -= prices[i]
                bought = True
            # si le lendemain on peut vendre plus cher, on attend
            if i < len(prices) - 1 and prices[i+1] > prices[i]:
                continue
            # sinon on vend
            total_profit += prices[i]
            bought = False
        return total_profit