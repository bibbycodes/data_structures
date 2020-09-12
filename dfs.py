from ds.py.stack import Stack
from ds.py.graph import Graph
from random import randint

def process(node, fn):
	fn(node.value)

def dfs_iterative(root):
	stack = Stack()
	visited = {}
	stack.push(root)

	while not stack.isEmpty():
		current_node = stack.pop()
		if current_node not in visited:
			visited[current_node] = True
			process(current_node, print)

		for node in current_node.children:
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
	random_index = randint(0, 5)
	root = list(g.nodes.keys())[0]

	dfs_iterative(root)

