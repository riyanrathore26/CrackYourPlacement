# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if node is None:
                return "#,"  # Marker for None
            return str(node.val) + "," + helper(node.left) + helper(node.right)
        
        return helper(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def helper(nodes):
            val = nodes.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper(nodes)
            node.right = helper(nodes)
            return node
        
        node_list = data.split(",")
        node_list.pop()
        return helper(node_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))