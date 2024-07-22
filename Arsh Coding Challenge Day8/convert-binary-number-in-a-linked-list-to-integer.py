# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int: # type: ignore
        st = ""
        while head != None:
            st += str(head.val)
            head = head.next
        return int(st,2)