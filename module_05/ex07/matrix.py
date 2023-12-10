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

    # def T(self):
    #     return self.data.T
    
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
        print(type(other))
        if isinstance(other, (int, float)):
            res = other * self.data
            return Matrix(res.tolist())
        # if isinstance(other, Vector):
            # ???
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
        
#     def __rtruediv__(self, other): # div : only scalars.
#         self.__truediv__(other)
        

class Vector(Matrix):

    def __init__(self, data):
        super().__init__(data) # init de data
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError("Invalid input for vector initialization")

    # def dot(self, other):
    #     if self.shape != other.shape:
    #         raise ValueError("Incompatible shapes for dot product")
    #     res = np.inner(self.values.flatten(), other.values.flatten()) # inner: produit scalair de deux vecteurs unidimensionnels. flatten: "applatit" au cas ou c'est des matrices 
    #     return res