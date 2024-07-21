# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        
        merged_root = TreeNode(root1.val + root2.val)
        
        def dfs(node1, node2, merged_node):
            if node1 and node2:
                if node1.left or node2.left:
                    merged_node.left = TreeNode((node1.left.val if node1.left else 0) + (node2.left.val if node2.left else 0))
                    dfs(node1.left, node2.left, merged_node.left)
                if node1.right or node2.right:
                    merged_node.right = TreeNode((node1.right.val if node1.right else 0) + (node2.right.val if node2.right else 0))  # type: ignore
                    dfs(node1.right, node2.right, merged_node.right)
            elif node1:
                if node1.left:
                    merged_node.left = TreeNode(node1.left.val)  # type: ignore
                    dfs(node1.left, None, merged_node.left)
                if node1.right:
                    merged_node.right = TreeNode(node1.right.val)  # type: ignore
                    dfs(node1.right, None, merged_node.right)
            elif node2:
                if node2.left:
                    merged_node.left = TreeNode(node2.left.val)  # type: ignore
                    dfs(None, node2.left, merged_node.left)
                if node2.right:
                    merged_node.right = TreeNode(node2.right.val)  # type: ignore
                    dfs(None, node2.right, merged_node.right)

        dfs(root1, root2, merged_root)
        return merged_root
