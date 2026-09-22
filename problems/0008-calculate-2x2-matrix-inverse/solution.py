def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
	[[a, b], [c, d]] = matrix

	det = a * d - b * c

	if not det:
		return None

	return [[d / det, -abs(b) / det], [-abs(c) / det, a / det]]