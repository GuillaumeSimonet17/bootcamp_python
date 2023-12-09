import matplotlib.pyplot as plt

def plot_with_loss(x, y, theta):
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
    # predict
    ones = np.ones_like(x)
    X = np.column_stack((ones, x))
    y_hat = np.dot(X, theta)

    # loss 
    m = 1/(2*y.size)
    
    
    plt.scatter(x, y, label='real data')
    plt.plot(x, y_hat, color='red', label='prediction')
    for i in range(y.size):
        dist = (y_hat[i] - y[i])**2
        loss = np.sum(m * dist)
        plt.plot([x[i], x[i]], [y[i], y_hat[i]], color='orange', linestyle='dotted', label='loss')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

import numpy as np
x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
# Example 1:
theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3)