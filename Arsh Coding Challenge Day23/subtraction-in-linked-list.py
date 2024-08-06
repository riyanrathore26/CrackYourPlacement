#User function Template for python3
class Node:
    def __init__(self,data)-> None:
        self.data = data 
        self.next = None
class Solution:
    def subLinkedList(self, l1, l2):
        num = num2 = 0
        while l1 or l2:
            if l1:
                num = num * 10 + l1.data
                l1 = l1.next
            if l2:
                num2 = num2 * 10 + l2.data
                l2 = l2.next
        nums =  abs(num-num2)
        dummy = Node(0)
        temp = dummy
        for i in range(1,3):
            temp.next = Node(nums * 10 // 10)
            temp = temp.next
        return temp
