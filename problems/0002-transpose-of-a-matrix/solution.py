def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a_t =[]
    for i in range(len(a[0])):
        a_t.append([])
        for j in range(len(a)):
            a_t[i].append(a[j][i])

    return a_t