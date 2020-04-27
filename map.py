from board import *
from road import *
from settlement import *

class Map:
	def __init__(self, board):
		self.board = board
		self.vertices = [None] * board.num_vertices
		self.edges = {}
		for edge in board.edges:
			self.edges[edge] = None
		self.knight_vertices = []

	def place_settlement(self, vertex, color, is_city):
		self.vertices[vertex] = Settlement(color, is_city)

	def can_place_settlement(self, vertex, color, is_city, is_connected):
		# settlements must be two road lengths from existing settlements (none on neighboring vertices)
		distance = True
		neighbors = self.board.neighbors[vertex]
		for n in neighbors:
			if self.vertices[n] != None:
				distance = False
		# settlements must be connected by roads
		connected = False
		for n in neighbors:
			e = (min(n, vertex), max(n, vertex))
			if self.edges[e] != None and self.edges[e].color == color:
				connected = True
		connected = connected or not is_connected
		# cities must replace existing settlements, settlements must replace blanks
		existing = False
		if is_city:
			existing = self.vertices[vertex] != None and self.vertices[vertex].color == color
		else:
			existing = self.vertices[vertex] == None
		just_settlement = distance and connected
		city_override = is_city or just_settlement
		return city_override and existing

	def place_road(self, side1, side2, color):
		self.edges[(min(side1, side2), max(side1, side2))] = Road(color)

	def can_place_road(self, side1, side2, color):
		# edge on one of the endpoints must match, or there must be a settlement
		connected = False
		neighbors1 = self.board.neighbors[min(side1, side2)]
		neighbors2 = self.board.neighbors[max(side1, side2)]
		color_on_end = None
		if self.vertices[min(side1, side2)] != None:
			color_on_end = self.vertices[min(side1, side2)].color
		if self.vertices[max(side1, side2)] != None:
			color_on_end = self.vertices[max(side1, side2)].color
		for n1 in neighbors1:
			e1 = (min(min(side1, side2), n1), max(min(side1, side2), n1))
			if self.edges[e1] != None and self.edges[e1].color == color:
				connected = True
		for n2 in neighbors2:
			e2 = (min(max(side1, side2), n2), max(max(side1, side2), n2))
			if self.edges[e2] != None and self.edges[e2].color == color:
				connected = True
		connected = connected or color_on_end == color
		# no edge existing
		no_existing = False
		road = self.edges[(min(side1, side2), max(side1, side2))]
		no_existing = road == None
		return connected and no_existing

	def place_knight(self, vertices):
		self.knight_vertices = vertices