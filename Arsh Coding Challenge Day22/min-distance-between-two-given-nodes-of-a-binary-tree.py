'''
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findLCA(self, root, n1, n2):
        if root is None:
            return None
        
        if root.data == n1 or root.data == n2:
            return root
        
        left_lca = self.findLCA(root.left, n1, n2)
        right_lca = self.findLCA(root.right, n1, n2)
        
        if left_lca and right_lca:
            return root
        
        return left_lca if left_lca is not None else right_lca
    
    def findDistanceFromLCA(self, root, target, distance):
        if root is None:
            return -1
        
        if root.data == target:
            return distance
        
        left_distance = self.findDistanceFromLCA(root.left, target, distance + 1)
        if left_distance != -1:
            return left_distance
        
        return self.findDistanceFromLCA(root.right, target, distance + 1)
    
    def findDist(self, root, a, b):
        lca = self.findLCA(root, a, b)
        print(lca.data)
        if lca is None:
            return -1
        
        distance_a = self.findDistanceFromLCA(lca, a, 0)
        distance_b = self.findDistanceFromLCA(lca, b, 0)
        
        return distance_a + distance_b