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

	def copy(self):
		c = Hand()
		c.num_lumber = self.num_lumber
		c.num_brick = self.num_brick
		c.num_wool = self.num_wool
		c.num_wheat = self.num_wheat
		c.num_ore = self.num_ore
		c.num_knights = self.num_knights
		c.num_victory_points = self.num_victory_points
		c.num_road_building = self.num_road_building
		c.num_year_of_plenty = self.num_year_of_plenty
		c.num_monopoly = self.num_monopoly
		c.num_knights_played = self.num_knights_played
		return c

	def __repr__(self):
		resources = (self.num_lumber, self.num_brick, self.num_wool, self.num_wheat, self.num_ore)
		dev_cards = (self.num_knights, self.num_victory_points, self.num_road_building, self.num_year_of_plenty, self.num_monopoly)
		return "Resources [L,B,W,Wh,O] " + repr(resources) + ", Cards [K,V,R,Y,M] " + repr(dev_cards)
