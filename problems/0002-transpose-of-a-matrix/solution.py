def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    size_of_one_arr = len(a[0])
    result = [[] for _ in range(size_of_one_arr)]
    i = 0

    while i < len(a):
        j = 0
        while j < len(a[i]):
            result[j].append(a[i][j])
            j += 1
        i += 1

    return result