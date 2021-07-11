"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = [0]
        profit += [(prices[i]-prices[i-1]) for i in range(1, n)]
        for i in range(1, n):
            profit[i] = max(profit[i]+profit[i-1], profit[i])
        
        return max(max(profit), 0)



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            profit = prices[i]-buy
            max_profit = max(max_profit, profit)
            
            buy = min(buy, prices[i])
        
        return max_profit