from development_card import *
from tile import *

class GameController:
	def __init__(self, map):
		self.map = map

	def take_n(self, hand, res, n):
		if res == TileType.MOUNTAINS:
			if hand.num_ore < n:
				return None
			hand.num_ore -= n
			return hand
		if res == TileType.PASTURE:
			if hand.num_wool < n:
				return None
			hand.num_wool -= n
			return hand
		if res == TileType.FOREST:
			if hand.num_lumber < n:
				return None
			hand.num_lumber -= n
			return hand
		if res == TileType.FIELDS:
			if hand.num_wheat < n:
				return None
			hand.num_wheat -= n
			return hand
		if res == TileType.HILLS:
			if hand.num_brick < n:
				return None
			hand.num_brick -= n
			return hand
		return None

	def trade_players(self, in_res, in_ratio, out_res, out_ratio, in_hand, out_hand):
		def do_trade(_in_res, _in_ratio, _out_res, _out_ratio, _in_hand, _out_hand):
			in_hand_tmp = _in_hand.copy()
			out_hand_tmp = _out_hand.copy()
			for i in range(len(_in_res)):
				in_hand_tmp = self.take_n(in_hand_tmp, _in_res[i], _in_ratio[i])
				out_hand_tmp = self.take_n(out_hand_tmp, _in_res[i], _in_ratio[i] * -1)
				if in_hand_tmp == None or out_hand_tmp == None:
					print("Trade " + str(i) + " failed... " + repr(in_hand_tmp) + " " + repr(out_hand_tmp))
					return None
			for i in range(len(_out_res)):
				out_hand_tmp = self.take_n(out_hand_tmp, _out_res[i], _out_ratio[i])
				in_hand_tmp = self.take_n(in_hand_tmp, _out_res[i], _out_ratio[i] * -1)
				if in_hand_tmp == None or out_hand_tmp == None:
					return None
			return (in_hand_tmp, out_hand_tmp)
		in_hand_copy = in_hand.copy()
		out_hand_copy = out_hand.copy()
		if do_trade(in_res, in_ratio, out_res, out_ratio, in_hand_copy, out_hand_copy) != None:
			return do_trade(in_res, in_ratio, out_res, out_ratio, in_hand, out_hand)
		return None

	def trade(self, in_res, out_res, ratio, hand, color):
		harbors = self.map.get_available_harbors(color)
		if ratio == 4:
			if self.take_n(hand, in_res, 4):
				self.take_n(hand, out_res, -1)
				return hand
			return None
		if ratio == 3:
			has_3 = False
			for harbor in harbors:
				if harbor.ratio == 3:
					has_3 = True
			if self.take_n(hand, in_res, 3):
				self.take_n(hand, out_res, -1)
				return hand
			return None
		if ratio == 2:
			has_2 = False
			for harbor in harbors:
				if harbor.resource == in_res:
					has_2 = True
			if self.take_n(hand, in_res, 2):
				self.take_n(hand, out_res, -1)
				return hand
			return None
		return None

	def has_largest_army(self, hand, color, other_hands):
		largest_army = hand.num_knights_played > 2
		for other_hand in other_hands:
			if other_hand.num_knights_played > hand.num_knights_played:
				largest_army = False
		return largest_army

	def find_longest_path_length(self, start, edges_of_color, possible_ends, visited):
		def edge_is_neighbor(edge1start, edge1end, edge2start, edge2end):
			if edge1start == edge2start:
				return edge1end != edge2end
			if edge1start == edge2end:
				return edge1end != edge2start
			if edge1end == edge2start:
				return edge1start != edge2end
			if edge1end == edge2end:
				return edge1start != edge2start
		start1, start2 = start
		length = 1
		if start in possible_ends and not start in visited:
			return 1
		for edge in edges_of_color:
			if edge in visited:
				continue
			edge1, edge2 = edge
			if not edge_is_neighbor(start1, start2, edge1, edge2):
				continue
			visited2 = visited.copy()
			visited2.append(edge)
			t_length = self.find_longest_path_length(edge, edges_of_color, possible_ends, visited2)
			length = max(length, 1 + t_length)
		return length

	def find_longest_road(self, color):
		# 1. Find all possible ends of a path
		#    Ends either have a noncolored road or a noncolored settlement
		edges_of_color = []
		possible_ends = []
		for edge in self.map.edges.keys():
			side1, side2 = edge
			is_end = False
			road = self.map.get_road(side1, side2)
			if road == None:
				continue
			if road.color == color:
				edges_of_color.append(edge)
				settlement1 = self.map.vertices[side1]
				settlement2 = self.map.vertices[side2]
				if settlement1 == None:
					if settlement2 != None and settlement2.color != color:
						is_end = True
				if settlement2 == None:
					if settlement1 != None and settlement1.color != color:
						is_end = True
				neighboring = self.map.get_neighboring_edges(side1, side2)
				for next_edge in neighboring:
					side3, side4 = next_edge
					next_road = self.map.get_road(side3, side4)
					if next_road == None or next_road.color != color:
						is_end = True
			if is_end:
				possible_ends.append(edge)
		# 2. From each end, branch out until another end
		#    Don't traverse visited edges again
		longest_routes = []
		for start in possible_ends:
			longest_routes.append(self.find_longest_path_length(start, edges_of_color, possible_ends, [start]))
		longest = 0
		for length in longest_routes:
			if length > longest:
				longest = length
		return longest

	def has_longest_road(self, color, other_colors):
		longest_road = self.find_longest_road(color)
		print("DEBUG -- Longest Road: " + str(longest_road))
		if longest_road < 5:
			return False
		for other_color in other_colors:
			if self.get_longest_road(other_color) > longest_road:
				return False
		return True

	def count_victory_points(self, hand, color, other_hands, other_colors):
		vp = 0
		# Settlements/Cities
		for v in range(self.map.board.num_vertices):
			settlement = self.map.vertices[v]
			if settlement == None:
				continue
			if settlement.color == color:
				if settlement.is_city:
					vp += 2
				else:
					vp += 1
		# Longest Road
		if self.has_longest_road(color, other_colors):
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
			if settlement != None:
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
		vertices, resources = self.map.board.get_vertices_and_resources_for_roll(roll)
		for i in range(len(vertices)):
			v = vertices[i]
			if v in self.map.knight_vertices:
				continue
			r = resources[i]
			s = self.map.vertices[v]
			if s != None and s.color == color:
				num_to_give = 2 if s.is_city else 1
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

	def collect_resources_all(self, roll, hands, colors):
		for i in range(len(hands)):
			self.collect_resources(roll, hands[i], colors[i])