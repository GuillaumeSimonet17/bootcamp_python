from matrix import Matrix, Vector
import numpy as np

m1 =    Matrix([[9.0, 1.0],
                [2.0, 3.0],
                [4.0, 5.0],
                [6.0, 7.0]])

m2 =    Vector([[7.0], [1.0], [3.], [4.]])

try:
    m3 = m1 * m2
    print((m3))
except Exception as e:
    print(e)
# a = np.array([[1, 2, 3],
# [4, 5, 6]])
# b = np.array([[2, 1, 3],
# [3, 2, 1]])
# print(a+b)
# m1 = Matrix([[0.0, 1.0, 2.0],
# [0.0, 2.0, 4.0]])
# v1 = Vector([[1], [2], [3]])
# m1 * v1

# # Or: Vector([[8], [16]
# v1 = Vector([[1], [2], [3]])
# v2 = Vector([[2], [4], [8]])
# v1 + v2
