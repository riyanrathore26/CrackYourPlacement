# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashTable = defaultdict(list)
        que = deque([(root, 0, 0)])  # (node, column, row)

        while que:
            node, col, row = que.popleft()
            if node:
                hashTable[col].append((row, node.val))
                que.append((node.left, col - 1, row + 1))
                que.append((node.right, col + 1, row + 1))

        sortedColumns = sorted(hashTable.items())
        result = []
        for col, values in sortedColumns:
            values.sort()
            result.append([val for row, val in values])

        return result
