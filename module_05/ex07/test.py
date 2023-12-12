from matrix import Matrix, Vector
import numpy as np

# m1 =    np.array([[0.0, 3.0, 5.],
#                 [5., 5.0, 2.0]])
# m2 =    Matrix([[0.0, 3.0, 5.],
#                 [5., 5.0, 2.0]])

# print(v1.shape)
# print(v2.shape)
try:
    v1 = Vector([[3], [4], [3]])
    v2 = Vector([[3], [4],[ 3]])
    m3 = v1.dot(v2)
    print((m3))

# try:
#     m3 = m2 * v1
#     print(m3)
#     # print((m2))
except Exception as e:
    print(e)
