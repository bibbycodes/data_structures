from random import random

class LinkedList:
	def __init__(self, head_value = None):
		self.head = Node(head_value) if head_value is not None else None

	def insert(self, value):
		if self.head:
			return self.head.insert(self.head, value)
		self.head = Node(value)
		return self.head

	def insert_in_order(self, value):
		if self.head is not None:
			if self.head.value > value:
				insert_node = Node(value)
				insert_node.next_node = self.head
				self.head = insert_node
				return self.head
			return self.head.insert_in_order(self.head, value)
		self.head = Node(value)
		return self.head

	def search(self, value):
		if not self.head:
			return None
		return self.head.search(value, self.head)

	def traverse(self):
		if self.head is not None:
			return self.head.traverse(self.head)
		print("linked list is empty")
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

	def insert_in_order(self, node, value):
		if node.value < value:
			if node.next_node == None:
				node.next_node = Node(value)
				return node.next_node
			if node.next_node.value > value:
				insert_node = Node(value)
				insert_node.next_node = node.next_node
				node.next_node = insert_node
				return insert_node
		return node.insert_in_order(node.next_node, value)

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