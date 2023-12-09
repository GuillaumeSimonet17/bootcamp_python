# MSE: mean squared error (Erreur quadratique moyenne)

def loss_(y, y_hat):
    """
    Computes the half mean squared error of two non-empty numpy.array, without any for loop.
    The two arrays must have the same dimensions.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        The half mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.array.
        None if y and y_hat does not share the same dimensions.
    Raises:
        This function should not raise any Exceptions.
    """
    m = 1/(2*y.size)
    dist = (y_hat - y)**2
    return np.sum(m * dist)


import numpy as np
X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
# Example 1:
print((loss_(X, Y)))
# Example 2:
loss_(X, X)
# Output: