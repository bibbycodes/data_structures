class Stack:
	def __init__(self, top = None):
		self.top = Node(top)
		self.size = 0

	def push(self, value):
		node = Node(value)
		node.previous = self.top
		self.top = node
		self.size += 1

	def pop(self):
		if self.size >= 1:
			popped = self.top
			self.top = self.top.previous
			self.size -= 1
			return popped.value
		raise Exception("Cannot pop, stack is empty")

	def peek(self):
		return self.top.value

	def is_empty(self):
		return self.size == 0

	def __repr__(self):
		node = self.top
		string_representation = ""
		while True:
			string_representation += f"{node.value}\n"
			if node.previous:
				node = node.previous
			else:
				break
		return string_representation



class Node():
	def __init__(self, value):
		self.value = value
		self.previous = None