class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def compute(self, head):
        # Reverse the linked list
        head = self.reverseList(head)
        
        max_node = head
        curr = head
        
        # Traverse the reversed list
        while curr and curr.next:
            if curr.next.data < max_node.data:
                curr.next = curr.next.next  # Delete the node
            else:
                curr = curr.next
                max_node = curr  # Update the max_node
                
        # Reverse the list again to restore original order
        head = self.reverseList(head)
        return head
