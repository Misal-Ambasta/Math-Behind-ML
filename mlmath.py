# mlmath.py

def dot_product(a, b):
    """
    Calculate the dot product of two equal-length vectors.

    Args:
        a (list of numbers): First vector.
        b (list of numbers): Second vector.

    Returns:
        float: The dot product of vectors a and b.

    Example:
        >>> dot_product([1, 2], [3, 4])
        11
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length.")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.

    Args:
        A (list of lists): Matrix A with dimensions m x n.
        B (list of lists): Matrix B with dimensions n x p.

    Returns:
        list of lists: Resulting matrix with dimensions m x p.

    Example:
        >>> matrix_multiply([[1, 2]], [[3], [4]])
        [[11]]
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            product_sum = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(product_sum)
        result.append(row)
    return result


def conditional_probability(events):
    """
    Calculate conditional probability P(A|B) = P(A and B) / P(B)

    Args:
        events (dict): A dictionary with keys:
            - "P(A and B)": Probability of both A and B occurring.
            - "P(B)": Probability of event B.

    Returns:
        float: Conditional probability P(A|B).

    Example:
        >>> conditional_probability({"P(A and B)": 0.12, "P(B)": 0.4})
        0.3
    """
    joint = events.get("P(A and B)")
    prob_b = events.get("P(B)")

    if prob_b == 0:
        raise ValueError("P(B) cannot be zero.")
    if joint is None or prob_b is None:
        raise ValueError("Both 'P(A and B)' and 'P(B)' must be provided.")

    return joint / prob_b
