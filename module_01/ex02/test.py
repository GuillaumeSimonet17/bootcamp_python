from vector import Vector
import numpy as np


def main():
    try:
        # ALL IS OK :
        # v1 = Vector(2, 9)
        # v2 = Vector(7)
        # v3 = Vector([[1.], [2.], [3.]])
        # v4 = Vector([1, 2, 3, 4, 5, 6])
        # v5 = Vector([4, 2, 2, 1, 5, 7])
        # v6 = Vector([[1.5], [2.2], [3.4]])
        # # print(v1.values, '\n')
        # # print(v2.values, '\n')
        # # print(v3.values, '\n')
        # # print(v4.values, '\n')

        # # print("v4 * v5 = ", v4.dot(v5))
        # # print("v3 * v6 = ", v3.dot(v6))
        # # print("v3 + v6 = \n", v3 + v6)
        # # print("v6 - v3 = \n", v6 - v3)
        # # print("v6 * 3 = \n", v6 * 10.5)
        # # print("v6 * v3 = \n", v6 * v3)
        # # print("v6 / 10 = \n", v6 / 10)

        # PROBLEMS :

        # v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        # v0 = v1.T()        #      me sort l'address de l'objet et non ca value
        # print(v0.values)   #      la c'est ok (donc l'obj est bon)
        # v1                 #      ca doit print grace a __repr__ mais ca marche po

        # RAISE ERR:
        print("v1 * v2", v1.dot(v2))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
