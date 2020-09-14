from ds.py.stack import Stack

print(Stack.__dict__)
# print(Stack.__dict__)
def process(node, fn):
	fn(node.value)

def dfs_iterative(root):
	stack = Stack()
	visited = {}
	stack.push(root)

	while not stack.isEmpty():
		current_node = stack.pop()
		if current_node not in visited:
			visted[current_node] = True
			process(current_node)

		for node in current_node.children():
			if node not in visited:
				stack.push(node)


