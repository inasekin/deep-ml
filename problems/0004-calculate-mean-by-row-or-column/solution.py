def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	if mode == 'column':
		result = []
		i = 0
		j = 0
		while i < len(matrix) and j < len(matrix[0]):
			if matrix[i][j] is not None:
				result.append(matrix[i][j])
			i += 1
			if len(result) == len(matrix):
				means.append(sum(result) / len(matrix))
				result = []
				j += 1
				i = 0

	if mode == 'row':
		for item in matrix:
			means.append(sum(item) / len(item))

	return means