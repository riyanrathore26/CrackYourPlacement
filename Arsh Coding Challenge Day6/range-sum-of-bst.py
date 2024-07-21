# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: # type: ignore
        count = 0
        def dfs(root):
            nonlocal count
            if root == None:
                return
            if root.val <= high and root.val >= low:
                count += root.val
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        return count