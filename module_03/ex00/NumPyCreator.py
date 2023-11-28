import numpy as np

class NumPyCreator:

    def contains(self, data, type):
        for sub in data:
            for item in sub:
                if isinstance(item, type):
                    return True
        return False
    
    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        l = len(lst[0])
        if all(len(sub) == l for sub in lst):
            if self.contains(lst, str):
                lst_str = [[str(item) for item in sub] for sub in lst]
                return np.array(lst_str, dtype='U21')
            return np.array(lst)

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        if not isinstance(itr, range):
            return None
        return np.array(itr)

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            return None
        return np.full(shape, value)

    def random(self, shape):
        if not isinstance(shape, tuple):
            return None
        return np.random.rand(*shape)
        
    def random_interval(self, shape, intervale=(0, 100)):
        if not isinstance(shape, tuple):
            return None
        return np.random.uniform(*intervale, shape)
        
    def identity(self, n):
        if not isinstance(n, int):
            return None
        shape = (n, n)
        return np.eye(*shape)


def main():
    obj = NumPyCreator()
    # lst = [[1, 2, 3], [6, 7, 8]]
    shape=(3,6)
    print(obj.random(shape))

if __name__ == "__main__":
    main()