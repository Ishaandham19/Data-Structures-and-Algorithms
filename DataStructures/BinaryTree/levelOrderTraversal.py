# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level_traversal = []
        queue = deque()
        queue.append(root)
        
        while len(queue):
            cur_level = []
            
            for i in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                         
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level_traversal.append(cur_level)
            
                
        return level_traversal
            
            
        
        