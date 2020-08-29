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

	def delete(self, value):
		node = self.search(value)
		if node == self.head:
			if self.head.next_node:
				self.head = self.head.next_node
				return self.head
			head = self.head
			self.head = None
			return head
		if node:
			parent_node = node.get_parent_node(self.head, value)
			if node.next_node:
				parent_node.next_node = node.next_node
			else:
				parent_node.next_node = None
		return node

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

	def get_parent_node(self, node, value, parent_node = None):
		if node.value == value:
			return parent_node
		if node.next_node == None:
			return None
		return node.get_parent_node(node.next_node, value, node)

l = LinkedList(2)
# for i in range(10):
# 	l.insert(round(random() * 1000))
node = l.insert(20)
l.insert(3)
l.insert(5)
deleted = l.delete(2)
l.traverse()

# previous = l.head.get_parent_node(l.head.next_node, 20)
# print("previous", previous.value)
# print(l.head.value)
# print(l.head.next_node.value)
