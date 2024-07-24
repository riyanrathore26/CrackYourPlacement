# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: # type: ignore
        result = []
        def findPair(node, k):
            if node is None or k < 0:
                return
            if k == 0:
                result.append(node.val)
                return
            findPair(node.left, k-1)
            findPair(node.right, k-1)
        def findTarget(root, target):
            if root is None:
                return -1
            if root.val == target.val:
                findPair(root, k)
                return 0
            left = findTarget(root.left, target)
            right = findTarget(root.right, target)
            if left != -1:
                if left + 1 == k:
                    result.append(root.val)
                else:
                    findPair(root.right, k - left - 2)
                return left + 1
            if right != -1:
                if right + 1 == k:
                    result.append(root.val)
                else:
                    findPair(root.left, k - right - 2)
                return right + 1
            return -1
        findTarget(root, target)
        return result