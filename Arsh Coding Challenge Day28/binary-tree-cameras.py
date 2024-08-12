class Tree:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None
def pri(root):
    if root == None:
        return
    left = pri(root.left)
    print(left)
    right = pri(root.right)
    print(right)
    return 1
obj = Tree(0)
obj.left = Tree(1)
obj.right = Tree(2)
# obj.left.left = Tree(3)
# obj.right.left = Tree(4)
# obj.left.right = Tree(5)
# obj.right.right = Tree(6)
pri(obj)