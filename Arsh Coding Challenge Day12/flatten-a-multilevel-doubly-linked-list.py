# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0)
        self.temp = dummy  # use self.temp instead of temp

        def dfs(node):
            while node:
                newNode = Node(node.val)
                self.temp.next = newNode
                newNode.prev = self.temp
                self.temp = newNode
                if node.child:
                    child_tail = dfs(node.child)
                    self.temp.next = child_tail.next
                    if child_tail.next:
                        child_tail.next.prev = self.temp
                    self.temp = child_tail
                node = node.next
            return self.temp

        dfs(head)
        dummy.next.prev = None
        return dummy.next
