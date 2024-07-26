# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        val1 = ""
        val2 = ""
        while l1 is not None:
            val1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            val2 += str(l2.val)
            l2 = l2.next
        val1,val2 = str(val1)[::-1],str(val2)[::-1]
        sums = int(val1) + int(val2)
        sums = str(sums)[::-1]
        dummy = ListNode(0)
        current = dummy
        for i in range(len(sums)):
            current.next = ListNode(int(sums[i]))
            current = current.next
        return dummy.next