from random import random

class LinkedList:
	def __init__(self, head_value = None):
		self.head = Node(head_value) if head_value else None

	def insert(self, value):
		if not self.head:
			self.head = Node(value)
			return self.head
		node = self.head
		while node.next_node:
			node = node.next_node
		node.next_node = Node(value)
		return node.next_node

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
		node = self.head
		while node:
			if node.value == value:
				return node
			node = node.next_node

	def traverse(self, func):
		node = self.head
		while node:
			func(node.value)
			node = node.next_node

	def delete(self, value):
		if self.head.value == value:
			self.head = self.head.next_node
		node = self.head
		previous = None
		while node:
			if node.value == value:
				previous = node
				previous.next_node = node.next_node
				return
			previous = node
			node = node.next_node

	def __repr__(self):
		if self.head:
			node = self.head
			node_string = str(node.value)
			while node.next_node:
				node_string = node_string + f" => {node.next_node.value}"
				node = node.next_node
			return node_string
		return "None"

class Node:
	def __init__(self, value):
		self.next_node = None
		self.value = value

	def __repr__(self):
		return str(self.value)

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

