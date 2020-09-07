from linked_list import LinkedList

class Graph:
	def __init__(self):
		self.nodes = {}

	def insert(self, node):
		self.nodes[node.value] = node.children

	def generate(self, graph_dict):
		for vertex_value in graph_dict.keys():
			node = Node(vertex_value)
			edges = graph_dict[vertex_value]
			for edge in edges:
				node.add_child(edge)
			self.insert(node)
			node.children = LinkedList()

class Node:
	def __init__(self, value):
		self.value = value
		self.children = LinkedList()

	def add_child(self, value):
		self.children.insert(value)

graph_dict = {
	0 : [1, 4, 5],
	1 : [4, 3],
	2 : [1],
	3 : [2, 4],
	4 : [],
	5 : []
}

g = Graph()
g.generate(graph_dict)
print(g.nodes)