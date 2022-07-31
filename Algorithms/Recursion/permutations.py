"""
Given an array nums of distinct integers, find all the possible permutations. 

Time Complexity - O(n! * n^2) is upper bound. 
Since n * n! is maximum nodes in tree (leaf row is n! and height of tree is n so this can be bounded by n *  n!)
And n is spent in each node.

Space Complexity - O(n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curPerms = []
        
        if len(nums) == 1:
            return [list(nums)]
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
            curPerms += perms
            nums.append(num)
        return curPerms
    
    
    
    
    