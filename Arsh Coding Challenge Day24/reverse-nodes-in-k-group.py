# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lists = []
        while head:
            lists.append(head.val)
            head = head.next

        i = 0
        while i + k - 1 < len(lists):
            l, r = i, i + k - 1
            while l < r:
                lists[l], lists[r] = lists[r], lists[l]
                l += 1
                r -= 1
            i += k

        dummy = ListNode(0)
        temp = dummy
        for val in lists:
            temp.next = ListNode(val)
            temp = temp.next

        return dummy.next
