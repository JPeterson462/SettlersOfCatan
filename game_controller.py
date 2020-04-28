class GameController:
	def __init__(self, map):
		self.map = map

	def has_largest_army(self, hand, color, other_hands):
		largest_army = hand.num_knights_played > 2
		for other_hand in other_hands:
			if other_hand.num_knights_played > hand.num_knights_played:
				largest_army = False
		return largest_army

	def has_longest_road(self, color):
		# TODO
		pass

	def count_victory_points(self, hand, color, other_hands):
		vp = 0
		# Settlements/Cities
		for v in range(self.map.board.num_vertices):
			settlement = self.map.vertices[v]
			if settlement.color == color:
				if settlement.is_city:
					vp += 2
				else:
					vp += 1
		# Longest Road
		if self.has_longest_road(color):
			vp += 2
		# Largest Army
		if self.has_largest_army(hand, color, other_hands):
			vp += 2
		# Victory Points
		vp += hand.num_victory_points
		return vp

	def buy_settlement(self, vertex, hand, color):
		if hand.num_brick < 1 or hand.num_lumber < 1 or hand.num_wheat < 1 or hand.num_wool < 1:
			return False
		if not self.map.can_place_settlement(vertex, color, False, True):
			return False
		hand.num_brick -= 1
		hand.num_lumber -= 1
		hand.num_wheat -= 1
		hand.num_wool -= 1
		self.map.place_settlement(vertex, color, False)
		return True

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
		if not self.map.can_place_road(edge1, edge2, color):
			return False
		hand.num_brick -= 1
		hand.num_lumber -= 1
		self.map.place_road(edge1, edge2, color)
		return True

	def buy_development_card(self, deck, hand):
		if hand.num_wheat < 1 or hand.num_ore < 1 or hand.num_wool < 1:
			return False
		if len(deck.deck) == 0:
			return False
		hand.num_wheat -= 1
		hand.num_ore -= 1
		hand.num_wool -= 1
		card = deck.draw()
		if card == DevelopmentCard.KNIGHT:
			hand.num_knights += 1
		if card == DevelopmentCard.VICTORY_POINT:
			hand.num_victory_points += 1
		if card == DevelopmentCard.ROAD_BUILDING:
			hand.num_road_building += 1
		if card == DevelopmentCard.YEAR_OF_PLENTY:
			hand.num_year_of_plenty += 1
		if card == DevelopmentCard.MONOPOLY:
			hand.num_monopoly += 1
		pass

	def play_knight(self, hand, type_r, roll):
		if hand.num_knights < 1:
			return (False, [])
		vertices = self.map.board.get_vertices_for_tile(type_r, roll)
		if sorted(vertices) == sorted(self.map.knight_vertices):
			return (False, []) # Cannot place where it already is
		self.map.place_knight(vertices)
		colors = []
		for v in vertices:
			settlement = self.map.vertices[v]
			colors.append(settlement.color)
		colors = list(set(colors))
		hand.num_knights -= 1
		hand.num_knights_played += 1
		return (True, colors)

	def play_road_building(self, hand, edge_pair1, edge_pair2, color):
		if hand.num_road_building < 1:
			return False
		edge1pair1, edge2pair1 = edge_pair1
		edge1pair2, edge2pair2 = edge_pair2
		if not self.map.can_place_road(edge1pair1, edge2pair1, color):
			return False
		if not self.map.can_place_road(edge1pair2, edge2pair2, color):
			return False
		self.map.place_road(edge1pair1, edge2pair1, color)
		self.map.place_road(edge1pair2, edge2pair2, color)
		hand.num_road_building -= 1
		return True

	def play_year_of_plenty(self, hand, card1, card2):
		if hand.num_year_of_plenty < 1:
			return False
		for r in [card1, card2]:
			if r == TileType.MOUNTAINS:
				hand.num_ore += 1
			if r == TileType.PASTURE:
				hand.num_wool += 1
			if r == TileType.FOREST:
				hand.num_lumber += 1
			if r == TileType.FIELDS:
				hand.num_wheat += 1
			if r == TileType.HILLS:
				hand.num_brick += 1
		hand.num_year_of_plenty -= 1
		return True

	def play_monopoly(self, hand, resource, other_hands):
		if hand.num_monopoly < 1:
			return False
		if r == TileType.MOUNTAINS:
			for other_hand in other_hands:
				hand.num_ore += other_hand.num_ore
				other_hand.num_ore = 0
		if r == TileType.PASTURE:
			for other_hand in other_hands:
				hand.num_wool += other_hand.num_wool
				other_hand.num_wool = 0
		if r == TileType.FOREST:
			for other_hand in other_hands:
				hand.num_lumber += other_hand.num_lumber
				other_hand.num_lumber = 0
		if r == TileType.FIELDS:
			for other_hand in other_hands:
				hand.num_wheat += other_hand.num_wheat
				other_hand.num_wheat = 0
		if r == TileType.HILLS:
			for other_hand in other_hands:
				hand.num_brick += other_hand.num_brick
				other_hand.num_brick = 0
		hand.num_monopoly -= 1
		return True

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