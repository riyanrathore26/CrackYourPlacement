# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for i in lists:
            while i != None:
                result.append(i.val)
                i = i.next
        dummy = ListNode(0)
        temp = dummy
        for i in sorted(result):
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next