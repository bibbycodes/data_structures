from ds.py.stack import Stack

def process(node, fn):
	fn(node.value)

def bfs(root):
	stack = Stack()
	visited = {}
	stack.push(root)

	while not stack.isEmpty():
		current_node = stack.pop()
		if current_node not in visited:
			visted[current_node] = True
			process(current_node, print)

		for node in current_node.children():
			if node not in visited:
				stack.push(node)