import numpy as np

# ∇(J) = 1/m X'T(X'θ − y)
# ∇(J) Vetcor 2
# X' MAtrix (m*2)
# X'T transpose of X' (2*m)
# y Vector (m,)
# θ Vector 2

# Careful : input x is Vector (m,)
# So transform x (m,) to fit dim of θ

# pourquoi T ? 
# - Optimisation de l'utilisation de la mémoire (si matrice BIG)
# - Multiplication de matrices (pour que ca colles, au shape en gros)
# - Manipulation de données : + pratique

def simple_gradient(x, y, theta):
    """
        Computes a gradient vector from three non-empty numpy.array, without any for loop.
        The three arrays must have compatible shapes.
        Args:
            x: has to be a numpy.array, a matrix of shape m * 1.
            y: has to be a numpy.array, a vector of shape m * 1.
            theta: has to be a numpy.array, a 2 * 1 vector.
        Return:
            The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
            None if x, y, or theta is an empty numpy.ndarray.
            None if x, y and theta do not have compatible dimensions.
        Raises:
            This function should not raise any Exception.
    """
    if not x.size or not y.size or not theta.size:
        return None
    # shape de x : m,1
    # shape de y : m,1
    # shape de theta : 2,1
    if x.ndim != 2 or y.ndim != 2 or x.shape[0] != y.shape[0] or (x.shape[1] != 1 or y.shape[1] != 1) or theta.shape != (2,1):
        return None
    res = np.zeros((2, 1))
    m = x.size
    Xp = np.column_stack((np.ones_like(x), x))
    XpT = Xp.T
    # print(theta)
    # print(Xp.shape)
    rr = [sum(i * theta) for i in Xp]   # Xp * theta
    rr = np.array(rr)
    # print(y.shape)
    # print(rr.shape)
    sub = [sum(i - y) for i in rr]      # rr - y

    # multiplier Xpt avec le resultat du produit de (Xp * theta) - y




x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434]).reshape((-1, 1))
# Example 0:
theta1 = np.array([[2], [0.7]])
# print(theta1)
print(simple_gradient(x, y, theta1))
# Output:
# array([[-19.0342...], [-586.6687...]])

# Example 1:
# theta2 = np.array([1, -0.4]).reshape((-1, 1))
# simple_gradient(x, y, theta2)
# Output:
# array([[-57.8682...], [-2230.1229...]])