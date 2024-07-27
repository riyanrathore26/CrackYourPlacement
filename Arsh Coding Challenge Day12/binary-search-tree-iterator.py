from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.que = deque()
        self._inorder(root)

    def _inorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        self._inorder(root.left)
        self.que.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        return self.que.popleft()

    def hasNext(self) -> bool:
        return len(self.que) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()