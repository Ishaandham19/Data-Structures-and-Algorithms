"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
and return the product.

Time Complexity - O(N)
Space Complexity - O(1)

Explanation: We track the max and min product values possible for a subsequence. This helps us use dp to determine the largest
prod for every element. 
"""

def maxProduct(self, nums: List[int]) -> int:
    minVal = nums[0]
    maxVal = nums[0]
    prod = nums[0]
    for val in nums[1:]:
        maxProd = val * maxVal
        maxVal = max(maxProd, val * minVal, val)
        minVal = min(val * minVal, maxProd, val)
        prod = max(maxVal, prod) 
    return prod