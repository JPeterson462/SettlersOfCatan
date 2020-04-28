from enum import Enum
import random

class DevelopmentCard(Enum):
	KNIGHT = 1
	ROAD_BUILDING = 2
	YEAR_OF_PLENTY = 3
	MONOPOLY = 4
	VICTORY_POINT = 5

class DevelopmentCardDeck:
	def __init__(self):
		self.deck = []
		for i in range(14):
			self.deck.append(DevelopmentCard.KNIGHT)
		for i in range(5):
			self.deck.append(DevelopmentCard.VICTORY_POINT)
		for i in range(2):
			self.deck.append(DevelopmentCard.ROAD_BUILDING)
			self.deck.append(DevelopmentCard.YEAR_OF_PLENTY)
			self.deck.append(DevelopmentCard.MONOPOLY)
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop(0)