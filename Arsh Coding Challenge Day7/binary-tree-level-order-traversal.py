from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            level_size = len(que)
            level_values = []
            for _ in range(level_size):
                node = que.popleft()
                level_values.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(level_values)
        return result