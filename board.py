class Board:
	def __init__(self, tiles):
		#     A1  A2  A3
		#   B1  B2  B3  B4
		# C1  C2  C3  C4  C5
		#   D1  D2  D3  D4
		#     E1  E2  E3
		a1, a2, a3 = [tiles[0][i] for i in (0, 1, 2)]
		b1, b2, b3, b4 = [tiles[1][i] for i in (0, 1, 2, 3)]
		c1, c2, c3, c4, c5 = [tiles[2][i] for i in (0, 1, 2, 3, 4)]
		d1, d2, d3, d4 = [tiles[3][i] for i in (0, 1, 2, 3)]
		e1, e2, e3 = [tiles[4][i] for i in (0, 1, 2)]
		# Populate a graph of vertices (cities and settlements) and edges (roads) for the standard 3-4 player board
		# by row, there are 7/9/11/11/9/7 vertices
		self.num_vertices = 54
		# by row, there are 6/4/8/5/10/6/10/5/8/4/6 edges
		self.num_edges = 72
		self.vertices = []
		self.edges = []
		def add_vertex(tiles_touching):
			self.vertices.append(tiles_touching)
		def add_edge(v1, v2):
			self.edges.append((v1, v2))
		# row 1
		add_vertex([a1])
		add_vertex([a1])
		add_vertex([a1, a2])
		add_vertex([a2])
		add_vertex([a2, a3])
		add_vertex([a3])
		add_vertex([a3])
		add_edge(0, 1)
		add_edge(1, 2)
		add_edge(2, 3)
		add_edge(3, 4)
		add_edge(4, 5)
		add_edge(5, 6)
		#...
		# row 2
		add_vertex([b1])
		add_vertex([b1, a1])
		add_vertex([b1, a1, b2])
		add_vertex([b2, a1, a2])
		add_vertex([b1])
		add_vertex([b1])
		add_vertex([b1])
		add_vertex([b1])
		add_vertex([b1])