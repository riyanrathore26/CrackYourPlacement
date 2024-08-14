class Solution:
    def largestBst(self, root):
        self.max_size = 0
        
        def dfs(node):
            if not node:
                # Return tuple (is_bst, size_of_bst, min_value_in_subtree, max_value_in_subtree)
                return (True, 0, float('inf'), float('-inf'))
            
            if not node.left and not node.right:
                # Leaf node is a valid BST by itself
                self.max_size = max(self.max_size, 1)
                return (True, 1, node.data, node.data)
            
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                size_of_bst = left_size + right_size + 1
                self.max_size = max(self.max_size, size_of_bst)
                return (True, size_of_bst, min(left_min, node.data), max(right_max, node.data))
            else:
                # If not a BST, return False with the largest subtree size (BST or not)
                return (False, max(left_size, right_size), 0, 0)
        
        dfs(root)
        return self.max_size
