# Solution ONE
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less = less_head
        greater = greater_head
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next
    
# Solution Two by my
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = []
        temp = []
        curr = head
        while curr is not None:
            if curr.val < x:
                result.append(curr.val)
            elif curr.val >= x:
                temp.append(curr.val)
            curr = curr.next
        dummy = ListNode(0)
        point = dummy
        for i in range(len(result)):
            point.next = ListNode(result[i])
            point = point.next
        for i in range(len(temp)):
            point.next = ListNode(temp[i])
            point = point.next
        return dummy.next
