import numpy as np

class Matrix:

    def __init__(self, arg):
        if isinstance(arg, list):
            self.matrix = np.array(arg)
        elif isinstance(arg, tuple):
            self.matrix = np.zeros(arg)
        self.shape = self.matrix.shape

    def __str__(self):
        return (f"{self.matrix.tolist()}")

    def T(self):
        return self.matrix.T
    
    def __add__(self, other): # add : only matrices of same dimensions.
        if not isinstance(other, Matrix):
            raise ValueError("C'est pas une matrice pelo....")
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        return Matrix(self.matrix + other.matrix)

    def __sub__(self, other): # sub : only matrices of same dimensions.
        if not isinstance(other, Matrix):
            raise ValueError("C'est pas une matrice pelo....")
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        return self.matrix - other.matrix

    def __mul__(self, other): # returns a Vector if we perform Matrix * Vector mutliplication.
        if isinstance(other, (int, float)):
            result = [[a * other for a in row] for row in self.matrix]
            return Matrix(result)
        elif isinstance(other, Vector):
            return self.__mul__(other.to_matrix())
        elif isinstance(other, Matrix) and self.shape[1] == other.shape[0]:
            other = other.T()
            print(other.shape)
            print(self.shape)
            return Matrix(other.matrix * self.matrix)

    def __truediv__(self, other): # div : only scalars.
        if isinstance(other, (int,float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return self.matrix / other
        
    def __rtruediv__(self, other): # div : only scalars.
        self.__truediv__(other)
        

class Vector(Matrix):

    def __init__(self, arg):
        super().__init__(arg) # init de matrix
        self.vector = arg

    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        res = np.inner(self.values.flatten(), other.values.flatten()) # inner: produit scalair de deux vecteurs unidimensionnels. flatten: "applatit" au cas ou c'est des matrices 
        return res