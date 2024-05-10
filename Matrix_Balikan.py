import numpy as np

def inverse_matrix(matrix):
    try:
        # Menggunakan fungsi inv dari NumPy untuk menghitung matriks balikan
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        # Jika matriks tidak memiliki balikan, raise exception
        raise ValueError("Matriks tidak memiliki balikan.")

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
    # Menghitung matriks balikan
    inv_matrix = inverse_matrix(matrix)
    print("\nInverse Matrix:")
    print_matrix(inv_matrix)
except ValueError as e:
    print("\nError:", e)
