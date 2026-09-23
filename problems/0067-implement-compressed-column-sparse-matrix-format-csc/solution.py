def compressed_col_sparse_matrix(dense_matrix):
    values = []
    row_indices = []
    column_pointer = [0]

    if len(dense_matrix) == 0:
        return values, row_indices, column_pointer

    num_rows = len(dense_matrix)
    num_cols = len(dense_matrix[0])

    i = 0
    j = 0
    pointer = 0

    while j < num_cols:
        while i < num_rows:
            if dense_matrix[i][j] != 0:
                values.append(dense_matrix[i][j])
                row_indices.append(i)
                pointer += 1
            i += 1
        column_pointer.append(pointer)
        i = 0
        j += 1

    return values, row_indices, column_pointer
