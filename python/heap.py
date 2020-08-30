class Heap:
	def __init__(self, capacity = 10):
		self.capacity = capacity
		self.size = 0
		self.items = []

	def get_left_child_index(parent_index):
		return 2 * parent_index + 1

	def get_right_child_index(parent_index):
		return 2 * parent_index + 2
	
	def get_parent_index(child_index):
		return (child_index - 1) / 2

	def has_left_child(parent_index):
		return get_left_child(parent_index) < self.size

	def has_right_child(parent_index):
		return get_right_child(parent_index) < self.size

	def get_left_child(parent_index):
		return items[get_rigth_child_index(parent_index)]

	def get_right_child(parent_index):
		return items[get_right_child_index(parent_index)]

	def get_parent(child_index):
		return items[get_parent_index(child_index)]

