from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        flag = 0
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
            if flag == 0:
                result.append(level_values)
                flag = 1
            elif flag == 1:
                result.append(level_values[::-1])
                flag = 0
        return result