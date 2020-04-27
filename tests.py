from board import *
from tile import *

# 0/6 7/15 16/26 27/37 38/46 47/53

test1 = False

# Test 1
if test1:
	# L O B S W D
	b1 = generate_board("OSLWBSBWLDLOLOWSBWS", [10, 2, 9, 12, 6, 4, 10, 9, 11, 0, 3, 8, 8, 3, 4, 5, 5, 6, 11])
	#print(str(b1.get_tiles_at(9)))
	#print(str(b1.get_tiles_at(44)))
	for i in range(54):
		print(b1.get_tiles_at(i))