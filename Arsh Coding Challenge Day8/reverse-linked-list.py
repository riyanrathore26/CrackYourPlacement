# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        pre = None
        curr = head
        while curr is not None:
            nx = curr.next
            curr.next = pre
            pre = curr
            curr = nx
        head = pre
        return head