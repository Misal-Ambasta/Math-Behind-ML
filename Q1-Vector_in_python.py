def add_vectors(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have equal length")
    return [a[i] + b[i] for i in range(len(a)) ]

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the equal length")
    return sum(a[i] * b[i] for i in range(len(a)))

def are_orthogonal(a,b):
    return dot_product(a, b)


a = [1, 2, 3]
b = [4, 5, 6]

print("Vector Operations:")
print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Sum: {add_vectors(a, b)}")
print(f"Dot Product: {dot_product(a, b)}")
print(f"Orthogonal: {are_orthogonal(a, b)}")
print()

# Matrix Multiplication Solution

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    rows_A = len(A)
    cols_B = len(B[0])
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        result.append(row)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(len(B)):
                result[i][j] +=A[i][k] * B[k][j]

    return result


def print_matrix(matrix, name):
    print(f"Matrix {name}:")
    for row in matrix:
        print(row)
    print()


A = [ [1,2], [3,4] ]
B = [ [5,6], [7,8] ]

print("Matrix Multiplication:")
print_matrix(A, "A")
print_matrix(B, "B")

result = multiply_matrices(A, B)
print_matrix(result, "A × B")