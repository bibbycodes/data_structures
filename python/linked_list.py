from random import random

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

	def traverse(self):
		if self.head:
			return self.head.traverse(self.head)
		return None

	# def delete(self, value):
	# 	node = self.search(value)
	# 	if node:
	# 		return node.delete()

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

	def traverse(self, node):
		print(node.perform_operation())
		if node.next_node == None:
			return
		return node.traverse(node.next_node)

	def perform_operation(self):
		return self.value

	

l = LinkedList(2)
for i in range(10):
	l.insert(round(random() * 1000))
l.traverse()

# print(l.head.value)
# print(l.head.next_node.value)
