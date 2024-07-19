# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        curr = head
        indx = 0
        while curr != None:
            indx +=1
            curr = curr.next
        mid = indx //2
        temp = head
        while mid != 0:
            mid -=1
            temp = temp.next
        return temp