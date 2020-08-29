class LinkedList:
	def __init__(self, head = None):
		self.head = head

	def insert(self, value):
		if self.head:
			return self.head.insert(self.head, value)


class Node:
	def __init__(self, value, next_node = None):
		self.next_node = next_node
		self.value = value

	def insert(self, node, value):
		if self.next_node == Node:
			self.next_node = Node(value)
		return self.insert(self.next, value)