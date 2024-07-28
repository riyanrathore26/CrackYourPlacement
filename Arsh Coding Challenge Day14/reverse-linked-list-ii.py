# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        
        i, j = left - 1, right - 1
        while i < j:
            result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1
        
        dummy = ListNode(0)
        temp = dummy
        for val in result:
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next