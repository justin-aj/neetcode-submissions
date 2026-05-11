class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        final = 0
        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] > prices[r]:
                l = r
            else:
                dif = prices[r] - prices[l]
                final = max(dif, final)
                print(final)
                r = r + 1
        return final



        """low = min(prices)
        inx = prices.index(low)
        for i in range(inx, len(prices)):
            print(i, prices[i], low)
            if prices[i] > low:
                low = prices[i]
        return low - prices[inx]"""
        