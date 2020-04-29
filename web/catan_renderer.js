class Tile {

	constructor(type, roll) {
		this.type = type;
		this.roll = roll;
	}

}

class HexMath {

	//     3
	//   4   2
	//   5   1
	//     0

	/*
		x + size, y
		x + size * 2 - offsety * 2, y;
		x + size * 3 - offsety * 4, y
		///
		x + size / 2 + offsety, y + size * 3 / 4
		x + size * 3 / 2 + offsety - offsety * 2, y + size * 3 / 4
		x + size * 5 / 2 + offsety - offsety * 4, y + size * 3 / 4
		x + size * 7 / 2 + offsety - offsety * 6, y + size * 3 / 4
		///
		x + offsety * 2, y + size * 6 / 4
		x + offsety * 2 + size - offsety * 2, y + size * 6 / 4
		x + offsety * 2 + size * 2 - offsety * 4, y + size * 6 / 4
		x + offsety * 2 + size * 3 - offsety * 6, y + size * 6 / 4
		x + offsety * 2 + size * 4 - offsety * 8, y + size * 6 / 4
		///
		x + size / 2 + offsety, y + size * 9 / 4
		x + size * 3 / 2 + offsety - offsety * 2, y + size * 9 / 4
		x + size * 5 / 2 + offsety - offsety * 4, y + size * 9 / 4
		x + size * 7 / 2 + offsety - offsety * 6, y + size * 9 / 4
		///
		x + size, y + size * 12 / 4
		x + size * 2 - offsety * 2, y + size * 12 / 4
		x + size * 3 - offsety * 4, y + size * 12 / 4
	*/

	static toRadians(degrees) {
		var pi = Math.PI;
		return degrees * (pi / 180);
	}
	static getPoint(centerx, centery, radius, index) {
		var angle = toRadians(30 + index * 60);
		var point = [ centerx + Math.sin(angle) * radius, centery + Math.cos(angle) * radius ];
		return point;
	}

	// 0/6 7/15 16/26 27/37 38/46 47/53
	static getVertexPositions(x, y, tile_width, tile_height, offsety) {
		//- 0 1 2 10 9 8
		//- _ 3 4 12 11 _
		//- _ 5 6 14 13 _
		//-- 7 _ _ 19 18 17
		//-- _ _ _ 21 20 _
		//-- _ _ _ * * _
		//-- _ _ * * * _
		//--- * _ _ * * *
		//--- _ _ _ * * _
		//--- _ _ _ * * _
		//--- _ _ _ * * _
		//--- _ _ * * * _
		//-- _ _ _ * * *
		//-- _ _ _ * * _
		//-- _ _ _ * * _
		//-- _ _ _ * * _
		//- _ _ _ * * *
		//- _ _ _ * * _
		//- _ _ _ * * _
	}

}

class Board {



}