from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Pointer to the buying day
        r = 1  # Pointer to the selling day
        total_max = 0  # Maximum profit

        while r < len(prices):
            # If the current profit is negative, move the buying day pointer to the selling day
            if prices[r] < prices[l]:
                l = r
            else:
                # Calculate profit and update total_max if profit is greater
                total_max = max(total_max, prices[r] - prices[l])
            r += 1  # Move the selling day pointer

        return total_max
