class Solution:
    def getCount(self, root, low, high):
        if root is None:
            return 0
        count = 0
        def dfs(node, low, high):
            nonlocal count
            if node is None:
                return
            if low <= node.data <= high:
                count += 1
            if node.data > low:
                dfs(node.left, low, high)
            if node.data < high:
                dfs(node.right, low, high)

        dfs(root, low, high)
        return count