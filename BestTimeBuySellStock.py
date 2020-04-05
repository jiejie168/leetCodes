__author__ = 'Jie'
"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        # naive method
        max_profit=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                profit=prices[j]-buy
                if profit>=max_profit:
                    max_profit=profit
        return max_profit

    def maxProfit_2(self,prices):
        # another efficient algorithm
        maxProfit=0
        minPrice=float("inf")  # "inf" is a positive infinitive.
        for price in prices:
            minPrice=min(minPrice,price)
            maxProfit=max(maxProfit,price-minPrice)
        return maxProfit


solution=Solution()
prices=[7,1,5,3,6,4]
ans=solution.maxProfit_2(prices)
print (ans)





