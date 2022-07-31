"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.

See explanation in resources/CombinationSum.pdf

Time Complexity : O(2^target)
Space Complexity : O(target)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def combinationSumHelper(index, curComb, curSum):
            if curSum == target:
                combinations.append(list(curComb))
                return
            if curSum > target or index >= len(candidates):
                return
                                    
            curComb.append(candidates[index])
            combinationSumHelper(index, curComb, curSum + candidates[index])
            curComb.pop()
            combinationSumHelper(index + 1, curComb, curSum)
            
        combinationSumHelper(0, [], 0)
        return combinations