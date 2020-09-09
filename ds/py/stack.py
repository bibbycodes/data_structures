class Stack:
	def __init__(self, top = None):
		self.top = top

	def push(self, node):
		node.previous = self.top
		self.top = node

	def pop(self):
		popped = self.top
		self.top = self.top.previous
		return popped

	def peek(self):
		return self.top.value

class Node():
	def __init__(self, value):
		self.value = value
		self.previous = None