from color import *

class Settlement:
	def __init__(self, color, is_city):
		self.color = color
		self.is_city = is_city
	def to_city(self):
		self.is_city = True