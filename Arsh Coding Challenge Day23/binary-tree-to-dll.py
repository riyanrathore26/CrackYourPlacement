class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def traverse(root, dll):
    if root is None:
        return dll
    dll = traverse(root.left, dll)
    new_dll_node = DLLNode(root.data)
    dll.next = new_dll_node
    new_dll_node.pre = dll
    dll = new_dll_node
    dll = traverse(root.right, dll)
    return dll

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    dummy = DLLNode(0)
    temp = dummy
    traverse(root, temp)

    # Printing the doubly linked list to verify
    current = dummy.next  # Skip the dummy node
    while current is not None:
        print(current.data, end=" ")
        current = current.next
