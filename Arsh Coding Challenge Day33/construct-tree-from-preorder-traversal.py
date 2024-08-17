class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def constructTree(pre, preLN, n):
    def build(pre, preLN, n, index):
        if index[0] >= n:
            return None

        node = Node(pre[index[0]])
        index[0] += 1

        if preLN[index[0] - 1] == 'L':
            return node

        node.left = build(pre, preLN, n, index)
        node.right = build(pre, preLN, n, index)

        return node

    # Using a list for index to maintain the state across recursive calls
    root = build(pre, preLN, n, index=[0])
    return root
