from enum import Enum
class TileType(Enum):
	MOUNTAINS = 1
	PASTURE = 2
	FOREST = 3
	FIELDS = 4
	HILLS = 5
	UNKNOWN = 6
	DESERT = 7

def get_tile_name(t):
	if t == TileType.MOUNTAINS:
		return ["Mountains", "Ore"]
	if t == TileType.PASTURE:
		return ["Pasture", "Wool"]
	if t == TileType.FOREST:
		return ["Forest", "Lumber"]
	if t == TileType.FIELDS:
		return ["Fields", "Wheat"]
	if t == TileType.HILLS:
		return ["Hills", "Brick"]
	if t == TileType.DESERT:
		return ["Desert", "Unknown"]
	return "Unknown"
def get_tile_type(t):
	# L O B S W D
	if t == "L":
		return TileType.FOREST
	if t == "O":
		return TileType.MOUNTAINS
	if t == "B":
		return TileType.HILLS
	if t == "S":
		return TileType.PASTURE
	if t == "W":
		return TileType.FIELDS
	if t == "D":
		return TileType.DESERT
	return TileType.UNKNOWN

class Tile:
	def __init__(self, type, roll):
		self.type = type
		self.roll = roll
	def __repr__(self):
		name = get_tile_name(self.type)
		return name[0] + " " + str(self.roll)