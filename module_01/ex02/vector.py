import numpy as np

class Vector:

    def __init__(self, values, v_range=None, shape=None):
        if isinstance(values, int):
            if v_range is not None:
                if values > v_range:
                    raise ValueError("a > b")
                self.values = np.arange(values, v_range, dtype=float).reshape((v_range - values, 1))
            else:
                self.values = np.array([float(i) for i in range(values)]).reshape((values, 1))
        else:
            self.values = np.array(values)
        self.shape = self.values.shape

    def __str__(self):
        return (f"{self.values.T.tolist()}")

    def dot(self, v2):
        if self.shape != v2.shape:
            raise ValueError("Incompatible shapes for dot product")
        res = np.inner(self.values.flatten(), v2.values.flatten()) # inner: produit scalair de deux vecteurs unidimensionnels. flatten: "applatit" au cas ou c'est des matrices 
        return res

    def T(self):
        return Vector(self.values.T)
    
    def __add__(self, v2):
        if not isinstance(v2, Vector):
            raise ValueError("C'est pas un vecteur pelo....")
        if self.shape != v2.shape:
            raise ValueError("Incompatible shapes for dot product")
        return self.values + v2.values

    def __sub__(self, v2):
        if not isinstance(v2, Vector):
            raise ValueError("C'est pas un vecteur pelo....")
        if self.shape != v2.shape:
            raise ValueError("Incompatible shapes for dot product")
        return self.values - v2.values

    def __mul__(self, scalar):
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            raise ValueError("C'est pas un scalaire pelo....")
        return self.values * scalar

    def __truediv__(self, scalar):
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            raise ValueError("C'est pas un scalaire pelo....")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.values / scalar

    def __rtruediv__(self, v2):
        return NotImplementedError("Division of a scalar by a Vector is not defined here.")