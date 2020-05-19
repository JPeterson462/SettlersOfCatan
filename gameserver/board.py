from tile import *

class Board:
	def get_tiles_at(self, vertex):
		return self.vertices[vertex]

	def get_vertices_and_resources_for_roll(self, roll):
		for_roll = []
		resources = []
		for v in range(self.num_vertices):
			for t in self.vertices[v]:
				if t.roll == roll:
					for_roll.append(v)
					resources.append(t.type)
		return (for_roll, resources)

	def get_vertices_for_tile(self, type_r, roll):
		for_roll = []
		for v in range(self.num_vertices):
			used = False
			for t in self.vertices[v]:
				if t.type == type_r and type_r == TileType.DESERT:
					used = True
				if t.roll == roll and t.type == type_r:
					used = True
			if used:
				for_roll.append(v)
		return for_roll

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
		self.neighbors = {}
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
		add_edge(0, 8)
		add_edge(2, 10)
		add_edge(4, 12)
		add_edge(6, 14)
		# row 2
		add_vertex([b1])
		add_vertex([b1, a1])
		add_vertex([b1, a1, b2])
		add_vertex([b2, a1, a2])
		add_vertex([b2, a2, b3])
		add_vertex([a2, a3, b3])
		add_vertex([a3, b3, b4])
		add_vertex([a3, b4])
		add_vertex([b4])
		add_edge(7, 8)
		add_edge(8, 9)
		add_edge(9, 10)
		add_edge(10, 11)
		add_edge(11, 12)
		add_edge(12, 13)
		add_edge(13, 14)
		add_edge(14, 15)
		add_edge(7, 17)
		add_edge(9, 19)
		add_edge(11, 21)
		add_edge(13, 23)
		add_edge(15, 25)
		# row 3
		add_vertex([c1])
		add_vertex([c1, b1])
		add_vertex([c1, b1, c2])
		add_vertex([c2, b1, b2])
		add_vertex([c2, c3, b2])
		add_vertex([c3, b2, b3])
		add_vertex([c3, c4, b3])
		add_vertex([c4, b3, b4])
		add_vertex([c4, c5, b4])
		add_vertex([c5, b4])
		add_vertex([c5])
		add_edge(16, 17)
		add_edge(17, 18)
		add_edge(18, 19)
		add_edge(19, 20)
		add_edge(20, 21)
		add_edge(21, 22)
		add_edge(22, 23)
		add_edge(23, 24)
		add_edge(24, 25)
		add_edge(25, 26)
		add_edge(16, 27)
		add_edge(18, 29)
		add_edge(20, 31)
		add_edge(22, 33)
		add_edge(24, 35)
		add_edge(26, 37)
		# row 4
		add_vertex([c1])
		add_vertex([c1, d1])
		add_vertex([c1, c2, d1])
		add_vertex([c2, d1, d2])
		add_vertex([c2, d2, c3])
		add_vertex([c3, d2, d3])
		add_vertex([c3, c4, d3])
		add_vertex([c4, d3, d4])
		add_vertex([c4, c5, d4])
		add_vertex([c5, d4])
		add_vertex([c5])
		add_edge(27, 28)
		add_edge(28, 29)
		add_edge(29, 30)
		add_edge(30, 31)
		add_edge(31, 32)
		add_edge(32, 33)
		add_edge(33, 34)
		add_edge(34, 35)
		add_edge(35, 36)
		add_edge(36, 37)
		add_edge(28, 38)
		add_edge(30, 40)
		add_edge(32, 42)
		add_edge(34, 44)
		add_edge(36, 46)
		# row 5
		add_vertex([d1])
		add_vertex([d1, e1])
		add_vertex([d1, d2, e1])
		add_vertex([d2, e1, e2])
		add_vertex([d2, d3, e2])
		add_vertex([d3, e2, e3])
		add_vertex([d3, d4, e3])
		add_vertex([d4, e3])
		add_vertex([d4])
		add_edge(38, 39)
		add_edge(39, 40)
		add_edge(40, 41)
		add_edge(41, 42)
		add_edge(42, 43)
		add_edge(43, 44)
		add_edge(44, 45)
		add_edge(45, 46)
		add_edge(39, 47)
		add_edge(41, 49)
		add_edge(43, 51)
		add_edge(45, 53)
		# row 6
		add_vertex([e1])
		add_vertex([e1])
		add_vertex([e1, e2])
		add_vertex([e2])
		add_vertex([e2, e3])
		add_vertex([e3])
		add_vertex([e3])
		add_edge(47, 48)
		add_edge(48, 49)
		add_edge(49, 50)
		add_edge(50, 51)
		add_edge(51, 52)
		add_edge(52, 53)
		# no down edges, bottom side
		for v in range(self.num_edges):
			self.neighbors[v] = []
		for edge in self.edges:
			start, end = edge
			self.neighbors[start].append(end)
			self.neighbors[end].append(start)
		for v in range(self.num_edges):
			self.neighbors[v] = list(set((self.neighbors[v])))

def generate_row(types, rolls):
	tiles = []
	for i in range(len(types)):
		tiles.append(Tile(get_tile_type(types[i]), rolls[i]))
	return tiles

def generate_board(types, rolls):
	r1 = generate_row(types[0:3], rolls[0:3])
	r2 = generate_row(types[3:7], rolls[3:7])
	r3 = generate_row(types[7:12], rolls[7:12])
	r4 = generate_row(types[12:16], rolls[12:16])
	r5 = generate_row(types[16:19], rolls[16:19])
	tiles = [r1, r2, r3, r4, r5]
	b = Board(tiles)
	return b