class LinkedList:
	def __init__(self, head = None):
		self.head = head

	def insert(self, value):
		if self.head:
			return self.head.insert(self.head, value)
		self.head = Node(value)


class Node:
	def __init__(self, value):
		self.next_node = None
		self.value = value

	def insert(self, node, value):
		if self.next_node == None:
			self.next_node = Node(value)
			return self.next_node
		return self.insert(self.next, value)

	

l = LinkedList()
l.insert(3)
l.insert(4)

print(l.head.value)
print(l.head.next_node.value)
