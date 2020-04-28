from board import *
from tile import *
from map import *
from color import *
from game_controller import *
from hand import *

# 0/6 7/15 16/26 27/37 38/46 47/53

test1 = False
test2 = True

# Test 1
if test1:
	# L O B S W D
	b1 = generate_board("OSLWBSBWLDLOLOWSBWS", [10, 2, 9, 12, 6, 4, 10, 9, 11, 0, 3, 8, 8, 3, 4, 5, 5, 6, 11])
	#print(str(b1.get_tiles_at(9)))
	#print(str(b1.get_tiles_at(44)))
	for i in range(54):
		print(b1.get_tiles_at(i))

if test2:
	b2 = generate_board("OSLWBSBWLDLOLOWSBWS", [10, 2, 9, 12, 6, 4, 10, 9, 11, 0, 3, 8, 8, 3, 4, 5, 5, 6, 11])
	m2 = Map(b2)
	m2.place_settlement(10, Color.RED, False)
	m2.place_settlement(29, Color.RED, False)
	m2.place_settlement(13, Color.ORANGE, False)
	m2.place_settlement(42, Color.ORANGE, False)
	m2.place_settlement(19, Color.WHITE, False)
	m2.place_settlement(35, Color.WHITE, False)
	m2.place_settlement(40, Color.BLUE, False)
	m2.place_settlement(44, Color.BLUE, False)
	m2.place_road(10, 11, Color.RED)
	m2.place_road(29, 30, Color.RED)
	m2.place_road(13, 12, Color.ORANGE)
	m2.place_road(42, 43, Color.ORANGE)
	m2.place_road(19, 18, Color.WHITE)
	m2.place_road(35, 24, Color.WHITE)
	m2.place_road(40, 41, Color.BLUE)
	m2.place_road(44, 34, Color.BLUE)
	m2.place_road(12, 4, Color.ORANGE)
	roads_red = 0
	roads_orange = 0
	roads_white = 0
	roads_blue = 0
	for e in m2.board.edges:
		v1, v2 = e
		if m2.can_place_road(v1, v2, Color.RED):
			roads_red += 1
		if m2.can_place_road(v1, v2, Color.ORANGE):
			roads_orange += 1
		if m2.can_place_road(v1, v2, Color.WHITE):
			roads_white += 1
		if m2.can_place_road(v1, v2, Color.BLUE):
			roads_blue += 1
	print("Placeable Roads: Red " + str(roads_red) + ", Orange " + str(roads_orange) + ", White " + str(roads_white) + ", Blue " + str(roads_blue))
	settlements_red = 0
	cities_red = 0
	settlements_orange = 0
	cities_orange = 0
	settlements_white = 0
	cities_white = 0
	settlements_blue = 0
	cities_blue = 0
	for v in range(m2.board.num_vertices):
		if m2.can_place_settlement(v, Color.RED, False, True):
			settlements_red += 1
		if m2.can_place_settlement(v, Color.RED, True, True):
			cities_red += 1
		if m2.can_place_settlement(v, Color.ORANGE, False, True):
			settlements_orange += 1
		if m2.can_place_settlement(v, Color.ORANGE, True, True):
			cities_orange += 1
		if m2.can_place_settlement(v, Color.WHITE, False, True):
			settlements_white += 1
		if m2.can_place_settlement(v, Color.WHITE, True, True):
			cities_white += 1
		if m2.can_place_settlement(v, Color.BLUE, False, True):
			settlements_blue += 1
		if m2.can_place_settlement(v, Color.BLUE, True, True):
			cities_blue += 1
	print("Placeable Settlements: Red " + str(settlements_red) + ", Orange " + str(settlements_orange) + ", White " + str(settlements_white) + ", Blue " + str(settlements_blue))
	print("Placeable Cities: Red " + str(cities_red) + ", Orange " + str(cities_orange) + ", White " + str(cities_white) + ", Blue " + str(cities_blue))
	gc2 = GameController(m2)
	print("Red's Longest Road")
	gc2.has_longest_road(Color.RED, [Color.ORANGE, Color.WHITE, Color.BLUE])
	print("Orange's Longest Road")
	gc2.has_longest_road(Color.ORANGE, [Color.RED, Color.WHITE, Color.BLUE])
	print("White's Longest Road")
	gc2.has_longest_road(Color.WHITE, [Color.ORANGE, Color.RED, Color.BLUE])
	print("Blue's Longest Road")
	gc2.has_longest_road(Color.BLUE, [Color.RED, Color.WHITE, Color.ORANGE])
	blue_hand2 = Hand()
	orange_hand2 = Hand()
	white_hand2 = Hand()
	red_hand2 = Hand()
	print("Orange VP: " + str(gc2.count_victory_points(red_hand2, Color.RED, [orange_hand2, white_hand2, blue_hand2], [Color.ORANGE, Color.WHITE, Color.BLUE])))
