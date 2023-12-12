import numpy as np

class Matrix:

    def __init__(self, arg):
        if isinstance(arg, list):
            self.data = np.array(arg)
            self.shape = (len(arg), len(arg[0]))
        elif isinstance(arg, tuple):
            self.data = np.zeros(arg)
            self.shape = arg

    def __str__(self):
        return (f"{self.data}")

    def T(self):
        res = []
        for col in zip(*self.data):
            res.append(col)
        return Matrix(res)
    
    def __add__(self, other): # add : only matrices of same dimensions.
        if not isinstance(other, Matrix):
            raise ValueError("C'est pas une matrice pelo....")
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        res = self.data + other.data
        return Matrix((res).tolist())

    def __sub__(self, other): # sub : only matrices of same dimensions.
        if not isinstance(other, Matrix):
            raise ValueError("C'est pas une matrice pelo....")
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        res = self.data - other.data
        return Matrix(res.tolist())

    def __mul__(self, other): # returns a Vector if we perform Matrix * Vector mutliplication.
        if isinstance(other, (int, float)):
            res = other * self.data
            return Matrix(res.tolist())
        if isinstance(other, Vector):
            if self.data.shape[1] == other.shape[0]:
                res = np.zeros((self.data.shape[0], other.shape[1]))
                for i in range(res.size):
                    for k in range(other.data.size):
                        res[i] += self.data[i][k]*other.data[k]
            return Vector(res.tolist())
        if isinstance(other, Matrix):
            if self.shape == other.shape: # Produit terme à terme (de Hadamard)
                res = other.data * self.data
                return Matrix(res.tolist())
            elif self.shape[0] == other.shape[1]:
                result = [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*other.data)] for row1 in self.data]
                if (other.shape[0] == 1):
                    return Vector(result)
                return Matrix(result)

    def __truediv__(self, other): # div : only scalars.
        if isinstance(other, (int,float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Matrix((self.data / other).tolist())

class Vector(Matrix):

    def __init__(self, data):
        super().__init__(data)
        # if self.data.shape[0] != 1 and self.data.shape[1] != 1:
            # raise ValueError("Invalid input for vector initialization")

    def __str__(self):
        return (f"{self.data}")

    def dot(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Incompatible shapes for dot product")
        res = np.inner(self.data.flatten(), other.data.flatten()) # inner: produit scalair de deux vecteurs unidimensionnels. flatten: "applatit" au cas ou c'est des matrices 
        if isinstance(res, (np.int64, np.float64)):
            r = [[res]]
            return Vector(r)