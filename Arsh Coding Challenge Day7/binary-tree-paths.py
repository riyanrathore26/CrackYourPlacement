from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                result.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return result
