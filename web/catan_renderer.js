class Tile {

	constructor(type, roll) {
		this.type = type;
		this.roll = roll;
	}

}

class HexMath {

	static TILE_SIZE = 160;
	static offsety = TILE_SIZE / 2 * (1 - Math.cos(Math.PI / 6));
	static TILE_WIDTH = 160 - offsety * 2;

	//     3
	//   4   2
	//   5   1
	//     0

	static toRadians(degrees) {
		var pi = Math.PI;
		return degrees * (pi / 180);
	}
	static getPoint(centerx, centery, radius, angle) {
		angle = toRadians(angle);
		var point = [ centerx + Math.sin(angle) * radius, centery + Math.cos(angle) * radius ];
		return point;
	}

	static fillVertexPositions(positions, indices, angles, x, y, row, column) {
		var columnOffsetsByRow = [ HexMath.TILE_SIZE, HexMath.TILE_SIZE / 2 + HexMath.offsety, HexMath.offsety * 2, HexMath.TILE_SIZE / 2 + HexMath.offsety, HexMath.TILE_SIZE ];
		var offsetysByRow = [ 0, HexMath.TILE_SIZE * 3 / 4, HexMath.TILE_SIZE * 6 / 4, HexMath.TILE_SIZE * 9 / 4, HexMath.TILE_SIZE * 1 / 4 ];
		var centerx = x + columnOffsetsByRow[row] + HexMath.TILE_WIDTH * column;
		var centery = y + offsetysByRow[row] + HexMath.TILE_SIZE / 2;
		for (var i = 0; i < indices.length; i++) {
			var index = indices[i];
			var angle = angles[i];
			positions[index] = getPoint(centerx, centery, HexMath.TILE_SIZE, angle);
		}
	}

	// 0/6 7/15 16/26 27/37 38/46 47/53
	static getVertexPositions(x, y) {
		// 240 180 120 60 0 300
		var vertices = [];
		//- 0 1 2 10 9 8
		fillVertexPositions(vertices, [0, 1, 2, 10, 9, 8], [240, 180, 120, 60, 0, 300], x, y, 0, 0);
		//- _ 3 4 12 11 _
		fillVertexPositions(vertices, [3, 4, 12, 11], [180, 120, 60, 0], x, y, 0, 0);
		//- _ 5 6 14 13 _
		fillVertexPositions(vertices, [5, 6, 14, 13], [180, 120, 60, 0], x, y, 0, 0);

		//-- 7 _ _ 19 18 17
		fillVertexPositions(vertices, [7, 19, 18, 17], [240, 60, 0, 300], x, y, 0, 0);
		//-- _ _ _ 21 20 _
		fillVertexPositions(vertices, [21, 20], [60, 0], x, y, 0, 0);
		//-- _ _ _ 23 22 _
		fillVertexPositions(vertices, [23, 22], [60, 0], x, y, 0, 0);
		//-- _ _ 15 25 24 _
		fillVertexPositions(vertices, [15, 25, 24], [120, 60, 0], x, y, 0, 0);

		//--- 16 _ _ 29 28 27
		fillVertexPositions(vertices, [16, 29, 28, 27], [240, 60, 0, 300], x, y, 0, 0);
		//--- _ _ _ 31 30 _
		fillVertexPositions(vertices, [31, 30], [60, 0], x, y, 0, 0);
		//--- _ _ _ 33 32 _
		fillVertexPositions(vertices, [33, 32], [60, 0], x, y, 0, 0);
		//--- _ _ _ 35 34 _
		fillVertexPositions(vertices, [35, 34], [60, 0], x, y, 0, 0);
		//--- _ _ 26 37 36 _
		fillVertexPositions(vertices, [26, 37, 36], [120, 60, 0], x, y, 0, 0);

		//-- _ _ _ 40 39 38
		fillVertexPositions(vertices, [40, 39, 38], [60, 0, 300], x, y, 0, 0);
		//-- _ _ _ 42 41 _
		fillVertexPositions(vertices, [42, 41], [60, 0], x, y, 0, 0);
		//-- _ _ _ 44 43 _
		fillVertexPositions(vertices, [44, 43], [60, 0], x, y, 0, 0);
		//-- _ _ _ 46 45 _
		fillVertexPositions(vertices, [46, 45], [60, 0], x, y, 0, 0);
		
		//- _ _ _ 49 48 47
		fillVertexPositions(vertices, [49, 48, 47], [60, 0, 300], x, y, 0, 0);
		//- _ _ _ 51 50 _
		fillVertexPositions(vertices, [51, 50], [60, 0], x, y, 0, 0);
		//- _ _ _ 53 52 _
		fillVertexPositions(vertices, [53, 52], [60, 0], x, y, 0, 0);

		return vertices;
	}

}

class Board {



}