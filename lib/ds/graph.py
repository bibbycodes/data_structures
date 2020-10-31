class Graph:
	def __init__(self, graph_dict = None):
		self.nodes = {}
		self.graph_dict = graph_dict
		if graph_dict:
			self.generate(graph_dict)

	def insert(self, node):
		self.nodes[node] = node.children

	def generate(self, graph_dict):
		dict_repr = {}
		# creates a dictionary of {node_value : Node} for each value in the graph dict
		[dict_repr.update({node_value : Node(node_value)}) for node_value in list(graph_dict.keys())] 
		for node_value in graph_dict.keys():
			node = dict_repr[node_value]
			edges = graph_dict[node_value]
			for edge in edges:
				node.add_child(dict_repr[edge])
			self.insert(node)

	def depth_first_search(self, root):
		if root == None:
			return
		self.visit(root, print)
		for node in self.nodes[root]:
			if node.visited == False:
				self.depth_first_search(node)

	def breadth_first_search(self, root):
		queue = []
		root.visited = True
		queue.insert(0, root)

		while len(queue) != 0:
			# pop from queue
			removed, queue = queue[-1], queue[:-1] 
			self.visit(removed, print)
			for node in removed.children:
				if node.visited == False:
					node.visited = True
					queue = [node] + queue

	def visit(self, node, fn):
		node.visited = True
		fn(node.value)

class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.visited = False

	def add_child(self, node):
		self.children.append(node)

	def __repr__(self):
		return str(self.value)
