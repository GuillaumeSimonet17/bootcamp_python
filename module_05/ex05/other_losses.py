# MSE: mean squared error (Erreur quadratique moyenne)
def mse_(y, y_hat):
    """
    Description:
        Calculate the MSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    m = 1/(y.size)
    dist = (y_hat - y)**2
    return m * np.sum(dist)

# RMSE: square root of MSE
def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        rmse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    m = 1/(y.size)
    dist = (y_hat - y)**2
    return np.sqrt(m * np.sum(dist))

# MAE: Mean absolute error
def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        mae: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    m = 1/(y.size)
    dist = abs(y_hat - y)
    return m * np.sum(dist)

def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        r2score: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    dist = np.sum((y_hat - y)**2)
    y_mean = np.mean(y)
    mean_dist = np.sum((y - y_mean)**2)
    if mean_dist == 0:
        return None
    return 1 - (dist / mean_dist)

import numpy as np
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
# Example 1:
x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
# Mean squared error
## your implementation
print(rmse_(x,y))
## Output: