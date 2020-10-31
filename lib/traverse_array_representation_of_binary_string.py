tree = [None,1,2,3,4,5,None,6,7,None,None,None,None,None,None,8]

def get_left_child_index(index):
	return (index * 2) + 1

def get_right_child_index(index):
	return (index * 2) + 2

def verify_index(index, arr):
	return True if index < len(arr) else False

def traverse(arr, index = 0):
	if arr[index] == None:
		return
	
	left_index = get_left_child_index(index)
	right_index = get_right_child_index(index)

	if verify_index(left_index, arr):
		traverse(arr, left_index)

	print(arr[index])

	if verify_index(right_index, arr):
		traverse(arr, right_index)

traverse(tree)
