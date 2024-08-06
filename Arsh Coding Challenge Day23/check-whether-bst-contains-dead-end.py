class Solution:
    def __init__(self):
        self.nodes = set()
        self.leaves = set()
        
    def store_nodes(self, root):
        if not root:
            return
        self.nodes.add(root.data)
        if root.left is None and root.right is None:
            self.leaves.add(root.data)
        self.store_nodes(root.left)
        self.store_nodes(root.right)

    def isDeadEnd(self, root):
        if not root:
            return False
        self.store_nodes(root)
        for leaf in self.leaves:
            if (leaf == 1 and 2 in self.nodes) or (leaf - 1 in self.nodes and leaf + 1 in self.nodes):
                return True
        return False
