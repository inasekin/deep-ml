import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	values_array = []
	indices_array = []
	row_pointes = [0]

	i = 0
	j = 0
	pointer = 0

	while i < len(dense_matrix):
		while j < len(dense_matrix[i]):
			if dense_matrix[i][j] != 0:
				values_array.append(dense_matrix[i][j])
				indices_array.append(j)
				pointer += 1
			j += 1
		row_pointes.append(pointer)
		j = 0
		i += 1

	return values_array, indices_array, row_pointes