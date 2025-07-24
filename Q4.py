'''
# Q: 4

## Create a Python Library

Build your own Python library **mlmath** with functions like:

- `dot_product(a, b)`
- `matrix_multiply(A, B)`
- `conditional_probability(events)`

Use proper docstrings and examples.
'''

import mlmath

print("Dot Product:", mlmath.dot_product([1, 2, 3], [4, 5, 6]))  # 32
print("Matrix Multiply:", mlmath.matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # [[19, 22], [43, 50]]
print("Conditional Probability:", mlmath.conditional_probability({
    "P(A and B)": 0.12,
    "P(B)": 0.4
}))  # 0.3
