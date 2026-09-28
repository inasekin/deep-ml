import numpy as np

def calculate_dot_product(vec1, vec2):
	result = 0
	if (len(vec1) != len(vec2)):
		return result

	i = 0

	while (i < len(vec1)):
		result += vec1[i] * vec2[i]
		i += 1
	
	return result
