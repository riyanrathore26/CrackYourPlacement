# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: # type: ignore
        count = 0

        def dfs(node, li):
            nonlocal count
            if not node:
                return
            li.append(node.val)
            path_sum = 0
            for i in range(len(li) - 1, -1, -1):
                path_sum += li[i]
                if path_sum == targetSum:
                    count += 1
            dfs(node.left, li)
            dfs(node.right, li)
            li.pop()
        dfs(root, [])
        return count
