def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = matrix
	i = 0
	j = 0

	while i < len(matrix):
		while j < len(matrix[i]):
			result[i][j] = matrix[i][j] * scalar
			j += 1
		j = 0
		i += 1
	
	return result
