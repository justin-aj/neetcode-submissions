class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxx = 0
        total_max = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                maxx = prices[r] - prices[l]
                total_max = max(total_max, maxx)
            r += 1
        return total_max

        