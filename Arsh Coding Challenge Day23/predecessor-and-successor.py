class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def findPreSuc(self, root,pre, suc,key):
        def findPredecessor(node):
            while node and node.right:
                node = node.right
            return node

        def findSuccessor(node):
            while node and node.left:
                node = node.left
            return node

        def findPreSucUtil(node):
            if not node:
                return

            if node.key == key:
                if node.left:
                    pre = findPredecessor(node.left)
                if node.right:
                    suc = findSuccessor(node.right)
            elif node.key > key:
                suc = node
                findPreSucUtil(node.left)
            else:
                pre = node
                findPreSucUtil(node.right)

        findPreSucUtil(root)
        return pre, suc

