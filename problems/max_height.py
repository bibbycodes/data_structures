import math
root = [None,1,2,3,4,5,None,6,7,None,None,None,None,None,None,8]

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def get_left_child_index(self, index):
		return (index * 2) + 1

	def get_right_child_index(self, index):
		return (index * 2) + 2

	def verify_index(self, index, arr):
		return True if index < len(arr) else False

	def make_node(self, index, arr):
		return TreeNode(arr[index]) if index < len(arr) else None

	def make_left(self, index, arr):
		left_index = self.get_left_child_index(index)
		return self.make_node(left_index, arr)

	def make_right(self, index, arr):
		right_index = self.get_right_child_index(index)
		return self.make_node(right_index, arr)

	def traverse(self, arr, index = 0):
		if arr[index] == None:
			return
		
		left_index = self.get_left_child_index(index)
		right_index = self.get_right_child_index(index)

		if self.verify_index(left_index, arr):
			self.traverse(arr, left_index)

		print(arr[index])

		if self.verify_index(right_index, arr):
			self.traverse(arr, right_index)

t = TreeNode()
t.traverse(root)
