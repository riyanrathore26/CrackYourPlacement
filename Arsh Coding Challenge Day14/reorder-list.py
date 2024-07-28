# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre,curr = None,slow
        while curr != None:
            nx = curr.next
            curr.next = pre
            pre = curr
            curr = nx
        first,second = head,pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next