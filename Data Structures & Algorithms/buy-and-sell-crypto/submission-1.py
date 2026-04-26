class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at any point if left < right you can calculate profit
        # if right > left (meaning sell is less than buy) you swap the buy
        # to current because you always want the lower buy price and then
        # increment r 
        maxP = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        
        return maxP
        