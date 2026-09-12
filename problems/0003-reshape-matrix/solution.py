import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    result = []
    rows, cols = new_shape

    flat_list = []
    for row in a:
        for element in row:
            flat_list.append(element)

    if len(flat_list) != rows * cols:
        return []

    index = 0
    for i in range(rows):
        new_row = []
        for j in range(cols):
            element = flat_list[index]
            new_row.append(element)
            index += 1
        result.append(new_row)

    return result