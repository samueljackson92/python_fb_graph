class Node:
	def __init__(self, data):
		self.adjacents = []
		self.data = data
		self.visited = False

	def add_adjacent(self, node):
		self.adjacents.append(node)

	def set_visited(self, state):
		self.visited = state

	def is_visited(self):
		return self.visited

class Graph:
	def __init__(self):
		self.nodes = {}

	def add_node(self, key, val):
		self.nodes[key] = val

	def add_adjacent(self, key, node):
		self.nodes[key].add_adjacent(node)

	def get_node(self, key):
		return self.nodes[key]