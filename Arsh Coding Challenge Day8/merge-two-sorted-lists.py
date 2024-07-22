# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        arr = []
        while list1 != None:
            arr.append(list1.val)
            list1 = list1.next
        while list2 != None:
            arr.append(list2.val)
            list2 = list2.next
        arr.sort()
        print(arr)
        dummy = ListNode(0)
        temp = dummy
        for i in range(len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return dummy.next