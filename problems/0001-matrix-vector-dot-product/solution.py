def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if (len(a) != len(b)): return -1
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result = []
	for m in a:
		if (isinstance(m, list)):
			i = 0
			result_sum = 0
			while (i < len(m)):
				result_sum = result_sum + (m[i] * b[i])
				i += 1
			
			result.append(result_sum)
		
	return result