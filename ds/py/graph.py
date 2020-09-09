from linked_list import LinkedList
from queue import Queue
from random import random
import math

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
		root.visited = True
		for node in self.nodes[root]:
			if node.visited == False:
				self.depth_first_search(node)

	def breadth_first_search(self, root):
		queue = []
		root.visited = True
		queue.append(root)

		while len(queue) != 0:
			removed, queue = queue[-1], queue[:-1]
			self.visit(removed, print)
			for node in removed.children:
				if node.visited == False:
					node.visited = True
					queue = [node] + queue

	def visit(self, node, fn):
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
# g.depth_first_search(root)
g.breadth_first_search(root)
print(g.nodes)