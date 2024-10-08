# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        if root == None:
            return []
        result = []
        def dfs(root,result):
            if root != None :
                dfs(root.left,result)
                result.append(root.val)
                dfs(root.right,result)
            return result
                
        return dfs(root,result)