# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: # type: ignore
        def dfs(node, currentSum):
            if node is None:
                return False
            
            currentSum += node.val
            
            # Check if it's a leaf node and the path sum equals targetSum
            if not node.left and not node.right:
                return currentSum == targetSum
            
            # Continue the search in the left and right subtrees
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        
        return dfs(root, 0)
