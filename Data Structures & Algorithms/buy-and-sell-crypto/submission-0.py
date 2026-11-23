class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n), Space:O(1)
        l, r = 0, 1 # l = Buy, r = Sell
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(prices[r] - prices[l], max_profit)
            else:
                l = r
            r += 1
        return max_profit
