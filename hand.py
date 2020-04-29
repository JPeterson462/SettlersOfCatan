class Hand:
	def __init__(self):
		self.num_lumber = 0
		self.num_brick = 0
		self.num_wool = 0
		self.num_wheat = 0
		self.num_ore = 0
		self.num_knights = 0
		self.num_victory_points = 0
		self.num_road_building = 0
		self.num_year_of_plenty = 0
		self.num_monopoly = 0
		self.num_knights_played = 0
	def __repr__(self):
		resources = (self.num_lumber, self.num_brick, self.num_wool, self.num_wheat, self.num_ore)
		dev_cards = (self.num_knights, self.num_victory_points, self.num_road_building, self.num_year_of_plenty, self.num_monopoly)
		return "Resources [L,B,W,Wh,O] " + repr(resources) + ", Cards [K,V,R,Y,M] " + repr(dev_cards)
