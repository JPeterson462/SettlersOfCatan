class GameController:
	def __init__(self, map):
		self.map = map

	def buy_settlement(self, vertex, hand, color):
		pass

	def buy_city(self, vertex, hand, color):
		if hand.num_ore < 3 or hand.num_wheat < 2:
			return False
		if not self.map.can_place_settlement(vertex, color, True, True):
			return False
		hand.num_ore -= 3
		hand.num_wheat -= 2
		self.map.place_settlement(vertex, color, True)
		return True

	def buy_road(self, edge1, edge2, hand, color):
		if hand.num_brick < 1 or hand.num_lumber < 1:
			return False
		# TODO
		return True

	def buy_development_card(self, deck, hand):
		pass

	def play_knight(self, hand, type, roll, color_to_steal):
		pass

	def play_road_building(self, hand, edge_pair1, edge_pair2):
		pass

	def play_year_of_plenty(self, hand, card1, card2):
		pass

	def play_monopoly(self, hand, resource, other_hands):
		pass

	def collect_resources(self, roll, hand, color):
		vertices, resources = self.map.get_vertices_and_resources_for_roll(roll)
		for i in range(len(vertices)):
			v = vertices[i]
			if v in self.map.knight_vertices:
				continue
			r = resources[r]
			s = self.map.vertices[v]
			if s.color == color:
				num_to_give = s.is_city ? 2 : 1
				if r == TileType.MOUNTAINS:
					hand.num_ore += num_to_give
				if r == TileType.PASTURE:
					hand.num_wool += num_to_give
				if r == TileType.FOREST:
					hand.num_lumber += num_to_give
				if r == TileType.FIELDS:
					hand.num_wheat += num_to_give
				if r == TileType.HILLS:
					hand.num_brick += num_to_give
		return True