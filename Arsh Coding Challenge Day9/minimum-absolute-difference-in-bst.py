# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # type: ignore
        mini = float('inf')
        prev = None
        def dfs(node):
            nonlocal mini, prev
            if not node:
                return
            dfs(node.left)
            if prev is not None:
                mini = min(mini, abs(node.val - prev.val))
            prev = node
            dfs(node.right)        
        dfs(root)
        return mini
