def initialize_mat(rows,col):
    mat = []
    for i in range(rows):
        mat.append([])
    for i in range(rows):
        for j in range(col):
            mat[i].append(0)
    return mat


def dot_product(u,v):
    dim1 = len(u)
    dim2 = len(v)
    ans = 0
    if dim1 == dim2:
        for i in range(dim1):
            ans += u[i]*v[i]
    return ans

def row_items(M,i):
    col = len(M[0])
    l = []
    for k in range(col):
        l.append(M[i][k])
    return l

def col_items(M,j):
    row = len(M)
    l = []
    for k in range(row):
        l.append(M[k][j])
    return l

def mat_mul(A,B):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])
    if col_A == row_B:
        C = initialize_mat(row_A,col_B)
        for i in range(col_A):
            for j in range(row_B):
                C[i][j] = dot_product(row_items(A,i),col_items(B,j))
    return C

M = [[1,2,3],[4,5,6],[8,9,0],[1,1,1],[4,2,4]]
N = [[5,2,3,4,1],[1,5,6,7,1],[8,2,2,7,6]]

print(mat_mul(M,N))