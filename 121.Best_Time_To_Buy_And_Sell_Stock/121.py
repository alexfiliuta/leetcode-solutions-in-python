class Solution(object):
    def maxProfit(self, prices):
        buy , sell = 0 , 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit , prices[sell]-prices[buy])
            else:
                buy = sell
            sell += 1
        return profit
        
        """
        :type prices: List[int]
        :rtype: int
        """
