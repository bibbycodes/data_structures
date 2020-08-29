class LinkedList:
	def __init__(self, head_value = None):
		self.head = Node(head_value)

	def insert(self, value):
		if self.head:
			return self.head.insert(self.head, value)
		self.head = Node(value)

	def search(self, value):
		if not self.head:
			return None
		return self.head.search(value, self.head)

class Node:
	def __init__(self, value):
		self.next_node = None
		self.value = value

	def insert(self, node, value):
		if node.next_node == None:
			node.next_node = Node(value)
			return node.next_node
		return node.insert(node.next_node, value)

	def search(self, value, node):
		if node.value == value:
			return node
		if node.next_node == None:
			return None
		return node.search(value, node.next_node)

	

l = LinkedList(2)
l.insert(3)
l.insert(4)
print(l.search(4).value)

print(l.head.value)
print(l.head.next_node.value)
