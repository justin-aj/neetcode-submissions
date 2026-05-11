class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        total_high = 0
        i = 0
        j = 1
        while i < len(prices) - 1 and j < len(prices):
            print(i, j)
            if prices[i] - prices[j] > 0:
                i = i + 1
                j = i + 1
            else:
                high = prices[j] - prices[i]
                j = j + 1
                total_high = max(total_high, high)
        return total_high



        """low = min(prices)
        inx = prices.index(low)
        for i in range(inx, len(prices)):
            print(i, prices[i], low)
            if prices[i] > low:
                low = prices[i]
        return low - prices[inx]"""
        """l, r = 0, len(prices) - 1
        final = 0
        while l < r:
            print(prices[r], prices[l])
            dif = prices[r] - prices[l]
            print(dif)
            final = max(dif, final)
            if dif < 0:
                l = l + 1
            else:
                r = r - 1
        return final"""