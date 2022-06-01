"""
Problem Statement
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Solution
In this problem we attempt to find a pair of values such that their difference is largest and the second value in the pair comes after the first in the array. 
A brute force way would be to check the largest pair of each value in the array and return the largest difference - O(N^2).
We can also use dynamic programming to attempt to solve this in O(N). 
Given [v1, v2, ... v_i-1, v_i, ... v_n], when at v_i we have track of "min" and "profit". 
At this point "min" should be the smallest element in [v1, v2 ... , v_i-1] as if v_i becomes the largest element in the profit pair only the minimum value in previous array ensures largest difference.
Also, if profit becomes large than its previous value we change it.

Complexity
Time Complexity - O(N)
Space Complexity - O(1)
"""

def maxProfit(prices: List[int]) -> int:
    profit = 0
    minP = prices[0]
    for i in range(1, len(prices)):
        minP = min(prices[i-1], minP)
        profit = max(profit, prices[i] - minP)
    return profit