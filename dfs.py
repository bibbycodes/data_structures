from ds.py.stack import Stack
from ds.py.graph import Graph
from random import randint

def process(node, fn):
	fn(node.value)

def dfs_iterative(root):
	stack = Stack()
	visited = {}
	stack.push(root)

	print(root)

	while not stack.is_empty():
		current_node = stack.pop()
		if current_node not in visited:
			visited[current_node] = True
			process(current_node, print)

		for node in current_node.children:
			print(node)
			if node not in visited:
				stack.push(node)


if __name__ == '__main__':
	graph_dict = {
		0 : [1, 4, 5],
		1 : [4, 3],
		2 : [1],
		3 : [2, 4],
		4 : [],
		5 : []
	}

	g = Graph(graph_dict)
	root = list(g.nodes.keys())[0]
	print(g.nodes)

	dfs_iterative(root)

