class MinHeap:
	def __init__(self, capacity = 10):
		self.capacity = capacity
		self.size = 0
		self.items = []

	def get_left_child_index(self, parent_index):
		if parent_index > self.size:
			raise IndexError("Index out of bounds")  
		return int(2 * parent_index + 1)

	def get_right_child_index(self, parent_index):
		if parent_index > self.size:
			raise IndexError("Index out of bounds")
		return int(2 * parent_index + 2)
	
	def get_parent_index(self, child_index):
		if child_index > self.size:
			raise IndexError("Index out of bounds")  
		return int((child_index - 1) / 2)

	def has_left_child(self, index):
		return self.get_left_child_index(index) < self.size

	def has_left_child_only(self, index):
		return self.has_left_child(index) and not self.has_right_child(index)

	def has_right_child_only(self, index):
		return self.has_right_child and not self.has_left_child(index)

	def has_right_child(self, index):
		return self.get_right_child_index(index) < self.size

	def has_parent(self, index):
		if index == 0:
			return False
		return self.get_parent_index(index) < self.size

	def get_left_child(self, parent_index):
		return self.items[(self.get_left_child_index(parent_index))]

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
			self.bubble_up()
			return value
		else:
			print("HEAP AT CAPACITY")

	def poll(self):
		if self.size == 0:
			print("Empty heap, cannot poll")
			return
		item = self.items[0]
		self.swap(0, self.size - 1)
		self.items = self.items[:-1]
		self.size -= 1
		self.bubble_down()
		return item

	def swap(self, index_one, index_two):
		temp = self.items[index_one]
		self.items[index_one] = self.items[index_two]
		self.items[index_two] = temp

	def bubble_up(self):
		index = self.size - 1
		value = self.items[0]
		while (self.items[index] < self.get_parent(index) and self.has_parent(index)):
			parent_index = self.get_parent_index(index)
			self.swap(parent_index, index)
			index = parent_index

	def bubble_down(self):
		index = 0
		while(self.has_left_child(index)):
			smaller_child_index = self.get_left_child_index(index)
			if (self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index)):
				smaller_child_index = self.get_right_child_index(index)
			if self.items[index] < self.items[smaller_child_index]:
				break
			else:
				self.swap(smaller_child_index, index)
			
			index = smaller_child_index
			

h = MinHeap(20)
item = h.insert(10)
h.insert(25)
# print(h.items)
h.insert(30)
# print(h.items)
h.insert(56)
# print(h.items)
h.insert(40)
# print(h.items)
h.insert(70)
# print(h.items)
h.insert(30)
# print(h.items)
h.insert(1)
# print(h.items)
h.insert(2)
print(h.items)
# print(h.get_parent_index(4))
# print(h.items)
h.poll()
# print(h.get_parent(2))
print(h.items)