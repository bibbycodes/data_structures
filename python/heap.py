class MinHeap:
	def __init__(self, capacity = 10):
		self.capacity = capacity
		self.size = 0
		self.items = []

	def get_left_child_index(self, parent_index):
		return int(2 * parent_index + 1)

	def get_right_child_index(self, parent_index):
		return int(2 * parent_index + 2)
	
	def get_parent_index(self, child_index):
		return int((child_index - 1) / 2)

	def has_left_child(self, parent_index):
		return self.get_left_child(parent_index) < self.size

	def has_right_child(self, parent_index):
		return self.get_right_child(parent_index) < self.size

	def get_left_child(self, parent_index):
		return self.items[(self.get_rigth_child_index(parent_index))]

	def get_right_child(self, parent_index):
		return self.items[(self.get_right_child_index(parent_index))]

	def get_parent(self, child_index):
		return self.items[(self.get_parent_index(child_index))]

	def insert(self, value):
		if self.size < self.capacity:
			if self.size == 0:
				self.items.append(value)
				self.size += 1
				return value
			self.items.append(value)
			self.size += 1
			return self.bubble_up(value, self.size - 1)
		else:
			print("HEAP AT CAPACITY")

	def bubble_up(self, value, index):
		parent_value = self.get_parent(index)
		if value > parent_value:
			return value
		if index == 0:
			return value
		parent_index = self.get_parent_index(index)
		self.items[parent_index] = value
		self.items[index] = parent_value
		print(self.items)
		return self.bubble_up(value, parent_index)

h = MinHeap(20)
item = h.insert(10)
h.insert(21)
h.insert(30)
h.insert(1)
h.insert(2)
print(h.get_parent_index(4))
print(h.items)