class Tile {

	constructor(type, roll) {
		this.type = type;
		this.roll = roll;
	}

}

class HexMath {

	static TILE_SIZE = 160;
	static offsety = HexMath.TILE_SIZE / 2 * (1 - Math.cos(Math.PI / 6));
	static TILE_WIDTH = 160 - HexMath.offsety * 2;

	static SETTLEMENT_RADIUS = 12;
	static CITY_RADIUS = 20;

	static ROBBER_SIZE = HexMath.TILE_SIZE / 4;

	//     3
	//   4   2
	//   5   1
	//     0

	static toRadians(degrees) {
		var pi = Math.PI;
		return degrees * (pi / 180);
	}
	static getPoint(centerx, centery, radius, angle) {
		angle = HexMath.toRadians(angle);
		var point = [ centerx + Math.sin(angle) * radius, centery + Math.cos(angle) * radius ];
		return point;
	}

	static flipPoint(centerx, centery, pointx, pointy, factor) {
		return [ centerx + (centerx - pointx) * factor, centery + (centery - pointy) * factor];
	}

	static fillVertexPositions(positions, indices, angles, x, y, row, column) {
		var columnOffsetsByRow = [ HexMath.TILE_SIZE, HexMath.TILE_SIZE / 2 + HexMath.offsety, HexMath.offsety * 2, HexMath.TILE_SIZE / 2 + HexMath.offsety, HexMath.TILE_SIZE ];
		var offsetysByRow = [ 0, HexMath.TILE_SIZE * 3 / 4, HexMath.TILE_SIZE * 6 / 4, HexMath.TILE_SIZE * 9 / 4, HexMath.TILE_SIZE * 12 / 4 ];
		var centerx = x + columnOffsetsByRow[row] + HexMath.TILE_WIDTH * column;
		var centery = y + offsetysByRow[row] + HexMath.TILE_SIZE / 2;
		for (var i = 0; i < indices.length; i++) {
			var index = indices[i];
			var angle = angles[i];
			positions[index] = HexMath.getPoint(centerx, centery, HexMath.TILE_SIZE / 2, angle);
		}
	}

	// 0/6 7/15 16/26 27/37 38/46 47/53
	static getVertexPositions(x, y) {
		// 240 180 120 60 0 300
		var vertices = [];
		//- 0 1 2 10 9 8
		HexMath.fillVertexPositions(vertices, [0, 1, 2, 10, 9, 8], [240, 180, 120, 60, 0, 300], x, y, 0, 0);
		//- _ 3 4 12 11 _
		HexMath.fillVertexPositions(vertices, [3, 4, 12, 11], [180, 120, 60, 0], x, y, 0, 1);
		//- _ 5 6 14 13 _
		HexMath.fillVertexPositions(vertices, [5, 6, 14, 13], [180, 120, 60, 0], x, y, 0, 2);

		//-- 7 _ _ 19 18 17
		HexMath.fillVertexPositions(vertices, [7, 19, 18, 17], [240, 60, 0, 300], x, y, 1, 0);
		//-- _ _ _ 21 20 _
		HexMath.fillVertexPositions(vertices, [21, 20], [60, 0], x, y, 1, 1);
		//-- _ _ _ 23 22 _
		HexMath.fillVertexPositions(vertices, [23, 22], [60, 0], x, y, 1, 2);
		//-- _ _ 15 25 24 _
		HexMath.fillVertexPositions(vertices, [15, 25, 24], [120, 60, 0], x, y, 1, 3);

		//--- 16 _ _ 29 28 27
		HexMath.fillVertexPositions(vertices, [16, 29, 28, 27], [240, 60, 0, 300], x, y, 2, 0);
		//--- _ _ _ 31 30 _
		HexMath.fillVertexPositions(vertices, [31, 30], [60, 0], x, y, 2, 1);
		//--- _ _ _ 33 32 _
		HexMath.fillVertexPositions(vertices, [33, 32], [60, 0], x, y, 2, 2);
		//--- _ _ _ 35 34 _
		HexMath.fillVertexPositions(vertices, [35, 34], [60, 0], x, y, 2, 3);
		//--- _ _ 26 37 36 _
		HexMath.fillVertexPositions(vertices, [26, 37, 36], [120, 60, 0], x, y, 2, 4);

		//-- _ _ _ 40 39 38
		HexMath.fillVertexPositions(vertices, [40, 39, 38], [60, 0, 300], x, y, 3, 0);
		//-- _ _ _ 42 41 _
		HexMath.fillVertexPositions(vertices, [42, 41], [60, 0], x, y, 3, 1);
		//-- _ _ _ 44 43 _
		HexMath.fillVertexPositions(vertices, [44, 43], [60, 0], x, y, 3, 2);
		//-- _ _ _ 46 45 _
		HexMath.fillVertexPositions(vertices, [46, 45], [60, 0], x, y, 3, 3);
		
		//- _ _ _ 49 48 47
		HexMath.fillVertexPositions(vertices, [49, 48, 47], [60, 0, 300], x, y, 4, 0);
		//- _ _ _ 51 50 _
		HexMath.fillVertexPositions(vertices, [51, 50], [60, 0], x, y, 4, 1);
		//- _ _ _ 53 52 _
		HexMath.fillVertexPositions(vertices, [53, 52], [60, 0], x, y, 4, 2);

		return vertices;
	}

}

class ClickManager {

	static getSettlementCityBounds(vertices, vertex) {
		var point = vertices[vertex];
		return Math.round(point[0]) + "," + Math.round(point[1]) + "," + HexMath.SETTLEMENT_RADIUS;
	}

	static addClickableAreas(vertices) {
		var area = document.createElement("area");
		area.setAttribute("shape", "circle");
		area.setAttribute("coords", ClickManager.getSettlementCityBounds(vertices, 0));
		area.setAttribute("href", "#0");
		document.getElementById("board").appendChild(area);
	}

}

class BoardRenderer {

	// 0/6 7/15 16/26 27/37 38/46 47/53
	static tileIndices = 	[ [0, 1, 2, 10, 9, 8], [2, 3, 4, 12, 11, 10], [4, 5, 6, 14, 13, 12],
						[7, 8, 9, 19, 18, 17], [9, 10, 11, 21, 20, 19], [11, 12, 13, 23, 22, 21], [13, 14, 15, 25, 24, 23],
					[16, 17, 18, 29, 28, 27], [18, 19, 20, 31, 30, 29], [20, 21, 22, 33, 32, 31], [22, 23, 24, 35, 34, 33], [24, 25, 26, 37, 36, 35],
					[28, 29, 30, 40, 39, 38], [30, 31, 32, 42, 41, 40], [32, 33, 34, 44, 43, 42], [34, 35, 36, 46, 45, 44],
						[39, 40, 41, 49, 48, 47], [41, 42, 43, 51, 50, 49], [43, 44, 45, 53, 52, 51]
						];

	static fills = {
		desert: "d4d66b",
		hills: "b8250f",
		forest: "0a5404",
		pasture: "86cc0c",
		mountains: "616375",
		fields: "e2f511",
		sea: "09a0db",
		red: "f00",
		orange: "ffa500",
		white: "fff",
		blue: "00f",
		robber: "000",
		any: "fff"
	};

	static getCenterOfTile(vertices, indices) {
		var totalx = 0;
		var totaly = 0;
		for (var i = 0; i < indices.length; i++) {
			var point = vertices[indices[i]];
			totalx += point[0];
			totaly += point[1];
		}
		return [totalx / indices.length, totaly / indices.length];
	}

	static drawSettlement(vertices, vertex, fill, ctx) {
		var point = vertices[vertex];
		ctx.strokeStyle = "#000";
		ctx.fillStyle = "#" + BoardRenderer.fills[fill];
		ctx.fillRect(point[0] - HexMath.SETTLEMENT_RADIUS, point[1] - HexMath.SETTLEMENT_RADIUS, HexMath.SETTLEMENT_RADIUS * 2, HexMath.SETTLEMENT_RADIUS * 2);
		ctx.strokeRect(point[0] - HexMath.SETTLEMENT_RADIUS, point[1] - HexMath.SETTLEMENT_RADIUS, HexMath.SETTLEMENT_RADIUS * 2, HexMath.SETTLEMENT_RADIUS * 2);
	}

	static drawCity(vertices, vertex, fill, ctx) {
		var point = vertices[vertex];
		var radius = HexMath.CITY_RADIUS;
		ctx.strokeStyle = "#000";
		ctx.fillStyle = "#" + BoardRenderer.fills[fill];
		ctx.beginPath();
		var start = HexMath.getPoint(point[0], point[1], radius, 180);
		ctx.moveTo(start[0], start[1]);
		for (var angle = 72; angle < 360; angle += 72) {
			var next = HexMath.getPoint(point[0], point[1], radius, angle + 180);
			ctx.lineTo(next[0], next[1]);
		}
		ctx.closePath();
		ctx.fill();
		ctx.stroke();
	}

	static drawHarbor(vertices, vertex1, neighbor1, vertex2, neighbor2, fill, ctx) {
		// static flipPoint(centerx, centery, pointx, pointy)
		var point1 = HexMath.flipPoint(vertices[vertex1][0], vertices[vertex1][1], vertices[neighbor1][0], vertices[neighbor1][1], 0.5);
		var point2 = HexMath.flipPoint(vertices[vertex2][0], vertices[vertex2][1], vertices[neighbor2][0], vertices[neighbor2][1], 0.5);
		var point3 = HexMath.flipPoint(vertices[vertex1][0], vertices[vertex1][1], vertices[neighbor1][0], vertices[neighbor1][1], 0.75);
		var point4 = HexMath.flipPoint(vertices[vertex2][0], vertices[vertex2][1], vertices[neighbor2][0], vertices[neighbor2][1], 0.75);
		ctx.fillStyle = "#" + BoardRenderer.fills[fill];
		ctx.beginPath();
		ctx.moveTo(point1[0], point1[1]);
		ctx.lineTo(point2[0], point2[1]);
		ctx.lineTo(point4[0], point4[1]);
		ctx.lineTo(point3[0], point3[1]);
		ctx.closePath();
		ctx.fill();
	}

	static drawRobber(vertices, row, column, ctx) {
		var offsetsByRow = [ 0, 3, 7, 12, 16 ];
		var tileIndicesForRow = BoardRenderer.tileIndices[offsetsByRow[row] + column];
		var center = BoardRenderer.getCenterOfTile(vertices, tileIndicesForRow);
		ctx.fillStyle = "#" + BoardRenderer.fills.robber;
		ctx.beginPath();
		ctx.arc(center[0], center[1], HexMath.ROBBER_SIZE / 2, 0, 2 * Math.PI, false);
		ctx.fill();
	}

	static drawRoad(vertices, vertex1, vertex2, fill, ctx) {
		var point1 = vertices[vertex1];
		var point2 = vertices[vertex2];
		ctx.lineWidth = 10;
		ctx.strokeStyle = "#" + BoardRenderer.fills[fill];
		ctx.beginPath();
		ctx.moveTo(point1[0], point1[1]);
		ctx.lineTo(point2[0], point2[1]);
		ctx.stroke();
		ctx.lineWidth = 1;
	}

	static drawTile(vertices, row, column, fill, roll, ctx) {
		var offsetsByRow = [ 0, 3, 7, 12, 16 ];
		var tileIndicesForRow = BoardRenderer.tileIndices[offsetsByRow[row] + column];

		ctx.strokeStyle = "#000";
		ctx.fillStyle = "#" + BoardRenderer.fills[fill];
		ctx.beginPath();
		var start = vertices[tileIndicesForRow[0]];
		ctx.moveTo(start[0], start[1]);
		for (var i = 1; i < tileIndicesForRow.length; i++) {
			var point = vertices[tileIndicesForRow[i]];
			ctx.lineTo(point[0], point[1]);
		}				
		ctx.closePath();
		ctx.fill();
		ctx.stroke();
		var center = BoardRenderer.getCenterOfTile(vertices, tileIndicesForRow);
		ctx.fillStyle = "#000";
		// for (var i = offset; i < 360; i += 60) {
		// 	drawRectAround(ctx, getPoint(centerx, centery, radius, i), 15, 15);
		// 	drawRectAround(ctx, getHalfwayPoint(centerx, centery, radius, i, i + 60), 15, 15);
		// }
		ctx.textAlign = "center";
		ctx.font = "32px Arial";
		if (roll == 6 || roll == 8) {
			ctx.fillStyle = "yellow";
		} else {
			ctx.fillStyle = "black";
		}
		if (roll != 7) {
			ctx.fillText(roll.toString(), center[0], center[1] + 12);
		}
		if (roll == 6 || roll == 8) {
			ctx.fillStyle = "black";
			ctx.strokeText(roll.toString(), center[0], center[1] + 12);
		}
	}

}