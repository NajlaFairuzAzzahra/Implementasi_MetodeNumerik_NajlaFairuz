import numpy as np

def lu_decomposition(matrix):
    n = len(matrix)
    # Inisialisasi matriks L dengan matriks identitas
    L = np.eye(n)
    # Inisialisasi matriks U dengan nol
    U = np.zeros((n, n))

    for k in range(n):
        # Mengisi elemen diagonal utama matriks U
        U[k, k] = matrix[k, k]
        # Mengisi elemen bagian atas matriks U dan elemen bawah matriks L
        for i in range(k + 1, n):
            L[i, k] = matrix[i, k] / U[k, k]
            U[k, i] = matrix[k, i]
        # Mengurangi matriks asli dengan hasil perkalian matriks L dan U
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                matrix[i, j] -= L[i, k] * U[k, j]

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
    # Melakukan dekomposisi LU
    L, U = lu_decomposition(matrix)
    print("\nLower Triangular Matrix (L):")
    print_matrix(L)
    print("\nUpper Triangular Matrix (U):")
    print_matrix(U)
except np.linalg.LinAlgError as e:
    print("\nError:", e)
