class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at any point if left < right you can calculate profit
        # if right > left (meaning sell is less than buy) you swap the buy
        # to current because you always want the lower buy price and then
        # increment r 

        maxProfit = 0
        l, r = 0, 1

        while l < r and r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        return maxProfit