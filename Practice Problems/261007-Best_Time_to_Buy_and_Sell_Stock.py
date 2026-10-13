# LeetCode
# 121. Best Time to Buy and Sell Stock

"""
Instruction

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        floor = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < floor:
                floor = prices[i]

            if prices[i] - floor > profit:
                profit = prices[i] - floor

        return profit