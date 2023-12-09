import numpy as np

def add_intercept(X):
    """Adds a column of 1's to the non-empty numpy.array x.
    Args:
        x: has to be a numpy.array of dimension m * n.
    Returns:
        X, a numpy.array of dimension m * (n + 1).
        None if x is not a numpy.array.
        None if x is an empty numpy.array.
    Raises:
        This function should not raise any Exception.
    """
    if not X.size > 0 or not isinstance(X, np.ndarray):
        return None
    O = np.ones_like(X) 
    C = np.column_stack((O, X)) # concat
    return C

X = np.array([1, 2, 3, 4])
print(add_intercept(X))