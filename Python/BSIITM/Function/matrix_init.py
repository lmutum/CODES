def initialize_mat(rows,col):
    mat = []
    for i in range(rows):
        mat.append([])
    for i in range(rows):
        for j in range(col):
            mat[i].append(0)
    return mat


print(initialize_mat(1,1))