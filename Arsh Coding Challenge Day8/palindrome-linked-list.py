# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # type: ignore
        val = ""
        while head != None:
            val += str(head.val)
            head = head.next
        if val == str(val)[::-1]:
            return True
        return False