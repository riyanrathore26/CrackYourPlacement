# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: # type: ignore
        dummy = ListNode(0)
        temp = dummy
        while head != None:
            if head.val == val:
                head = head.next
            else:
                temp.next = ListNode(head.val)
                temp = temp.next
                head = head.next
        return dummy.next