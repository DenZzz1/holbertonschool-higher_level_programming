def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.
    
    Args:
        matrix: A 2-dimensional array of integers
        
    Returns:
        A new matrix with squared values, same size as input matrix
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
