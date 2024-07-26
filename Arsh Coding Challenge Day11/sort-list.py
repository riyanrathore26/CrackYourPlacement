from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        dummy = ListNode(0)
        current = dummy
        while head!=None:
            li.append(head.val)
            head=head.next
        for i in sorted(li):
            current.next = ListNode(i)
            current = current.next
        return dummy.next