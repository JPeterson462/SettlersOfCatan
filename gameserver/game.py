from color import *
import random

class Pieces:
	def __init__(self, color):
		self.num_settlements = 5
		self.num_cities = 4
		self.num_roads = 15
		self.color = color

class Game:
	def __init__(self, num_players):
		#   1
		# 4   2
		#   3

		# Choose order
		self.colors = [Color.WHITE, Color.ORANGE, Color.BLUE, Color.RED]
		who_can_go_first = range(1, num_players + 1)
		while len(who_can_go_first) > 1:
			next_round = []
			rolls = []
			for i in range(len(who_can_go_first)):
				rolls.append(self.roll_dice(1))
			max_num	= max(rolls)
			for i in range(len(who_can_go_first)):
				if rolls[i] == max_num:
					next_round.append(who_can_go_first[i])
			who_can_go_first = next_round
		self.who_starts = who_can_go_first[0]
		# Generate board
		possible_tiles = [ TileType.DESERT, TileType.MOUNTAINS, TileType.MOUNTAINS, TileType.MOUNTAINS, TileType.PASTURE, TileType.PASTURE, TileType.PASTURE, TileType.PASTURE, TileType.FOREST, TileType.FOREST, TileType.FOREST, TileType.FOREST, TileType.FIELDS, TileType.FIELDS, TileType.FIELDS, TileType.FIELDS, TileType.HILLS, TileType.HILLS, TileType.HILLS ]
		possible_rolls = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12 ]
		# TODO

	def roll_dice(self, count):
		total = 0
		for i in range(count):
			total += random.randint(1, 6)
		return total
