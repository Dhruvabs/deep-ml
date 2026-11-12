import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    A_L= A.tolist()
    B_L=b.tolist()
    x = np.zeros(len(B_L))
    for i in range(n):
        x_new = np.zeros(len(B_L))
        for i in range(len(A_L)):
            s= 0
            for j in range(len(A_L[0])):
                if j!=i:
                    s += A_L[i][j]*x[j]
            x_new[i] = (B_L[i]-s)/A_L[i][i]
        x=x_new
    return x.tolist()