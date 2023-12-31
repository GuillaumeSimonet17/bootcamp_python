import matplotlib.pyplot as plt

def plot(x, y, theta):
    """
        Plot the data and prediction line from three non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of dimension m * 1.
        y: has to be an numpy.array, a vector of dimension m * 1.
        theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exceptions.
    """
    ones = np.ones_like(x)
    X = np.column_stack((ones, x))
    y_hat = np.dot(X, theta)
    
    plt.scatter(x, y, label='real data')
    plt.plot(x, y_hat, color='red', label='prediction')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


import numpy as np
x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
# Example 1:
theta3 = np.array([[3],[.6]])
plot(x, y, theta3)