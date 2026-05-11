class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        min_price = prices[0]
        max_prof = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_prof = max(max_prof, prices[i] - min_price)

        return max_prof
