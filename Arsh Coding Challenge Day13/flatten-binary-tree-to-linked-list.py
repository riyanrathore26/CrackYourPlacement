# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None: # type: ignore
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(root):
            if root == None:
                return
            dfs(root.right)
            dfs(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        dfs(root)