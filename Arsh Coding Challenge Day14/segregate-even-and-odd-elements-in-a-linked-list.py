# Python program to segregate even and odd nodes
# in a Linked List

# A node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def p(node):
    while(node is not None):
        print(node.data, end=" ")
        node = node.next

def divide(head):
    q = []
    qe = []
    qo = []
    cur = head
    while(cur is not None):
        if(cur.data % 2 == 0):
            qe.append(cur)
        else:
            qo.append(cur)
        cur = cur.next

    node = Node(-100)
    ans = node

    while(len(qe) > 0):
        q.append(qe.pop(0))

    while(len(qo) > 0):
        q.append(qo.pop(0))

    while(len(q) > 0):
        node.next = q.pop(0)
        node = node.next

    node.next = None
    return ans.next

head = Node(9)
head.next = Node(1)
head.next.next = Node(6)
head.next.next.next = Node(7)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)
temp = divide(head)
p(temp)

# This code is contributed by Yash Agarwal(yashagrwal2852002)
