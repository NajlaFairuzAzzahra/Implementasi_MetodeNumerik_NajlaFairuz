import numpy as np

def crout_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.eye(n)

    for k in range(n):
        L[k, k] = 1
        for j in range(k, n):
            U[k, j] = matrix[k, j] - sum(L[k, i] * U[i, j] for i in range(k))
        for i in range(k + 1, n):
            L[i, k] = (matrix[i, k] - sum(L[i, j] * U[j, k] for j in range(k))) / U[k, k]

    return L, U

# Fungsi untuk mencetak matriks
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriks contoh
matrix = np.array([[1, 2],
                    [3, 4]])


print("Matrix:")
print_matrix(matrix)

try:
    # Melakukan dekomposisi Crout
    L, U = crout_decomposition(matrix)
    print("\nLower Triangular Matrix (L):")
    print_matrix(L)
    print("\nUpper Triangular Matrix (U):")
    print_matrix(U)
except np.linalg.LinAlgError as e:
    print("\nError:", e)
