from typing import Optional


class Solution:
    def __init__(self):
	    self.diameter = 0  # stores the maximum diameter calculated
	
    def depth(self, node: Optional[TreeNode]) -> int: # type: ignore

        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        
        # Calculate diameter
        self.diameter = max(self.diameter, left + right)
        
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int: # type: ignore
        self.depth(root)
        return self.diameter