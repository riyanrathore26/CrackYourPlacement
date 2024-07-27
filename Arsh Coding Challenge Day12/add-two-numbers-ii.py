# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1 or l2:
            if l1:
                num1 = num1 * 10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2 * 10 + l2.val
                l2 = l2.next
        total = num1 + num2
        dummy = ListNode(0)
        temp = dummy
        if total == 0:
            return ListNode(0)
        for i in str(total):
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next