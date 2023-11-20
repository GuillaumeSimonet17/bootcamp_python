from vector import Vector
import numpy as np


def main():
    try:
        v1 = Vector(3, 9)
        v2 = Vector(7)
        v3 = Vector([[1.], [2.], [3.]])
        v4 = Vector([1, 2, 3, 4, 5, 6])
        print(v1.values, '\n')
        print(v2.values, '\n')
        print(v3.values, '\n')
        print(v4.values, '\n')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
