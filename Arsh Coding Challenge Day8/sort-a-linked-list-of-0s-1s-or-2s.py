# Define a class for a node in a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to insert a new node at the end of the linked list


def push(head, data):
	new_node = Node(data)

	if head is None:
		head = new_node
		return head

	last = head
	while last.next is not None:
		last = last.next

	last.next = new_node
	return head

# Function to print the linked list


def printList(head):
	current = head
	while current is not None:
		print(current.data, end=' ')
		current = current.next
	print()

# Function to sort the linked list containing 0's, 1's, and 2's


def sortList(head):
	count = [0, 0, 0]

	# Count the number of 0's, 1's, and 2's in the linked list
	current = head
	while current is not None:
		count[current.data] += 1
		current = current.next

	# Overwrite the linked list with the sorted elements
	current = head
	i = 0
	while current is not None:
		if count[i] == 0:
			i += 1
		else:
			current.data = i
			count[i] -= 1
			current = current.next


# Main function to test the implementation
if __name__ == '__main__':
	head = None

	# Insert some elements into the linked list
	head = push(head, 0)
	head = push(head, 1)
	head = push(head, 0)
	head = push(head, 2)
	head = push(head, 1)
	head = push(head, 1)
	head = push(head, 2)
	head = push(head, 1)
	head = push(head, 2)

	print("Linked List before Sorting:")
	printList(head)

	sortList(head)

	print("Linked List after Sorting:")
	printList(head)
