__author__ = 'Jie'
"""
Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""

class Solution:
    def maxProfit(self, prices) -> int:
        # method 1
        # add the consecutive value, as long as the later is larger than the former.
        maxProfit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxProfit +=prices[i]-prices[i-1]
        return maxProfit
    def maxProfit_1(self,prices):
        # method 2, to fine the consecutive vally and peak points
        # and then sum together.
        maxProfit=0
        i=0
        peak=prices[0]
        valle=prices[0]
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            valle=prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
            peak=prices[i]
            maxProfit +=peak-valle
        return maxProfit

solution=Solution()
prices=[7,1,5,3,6,4]
ans=solution.maxProfit_1(prices)
print (ans)